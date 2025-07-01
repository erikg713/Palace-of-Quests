import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import supabase from './supabase.js';
import { approvePayment, completePayment, getPayment } from './pi.js';

const app = express();
app.use(cors());
app.use(express.json());

// Health check
app.get('/api/health', (_, res) => res.json({ ok: true }));

// Get user from Supabase
app.get('/api/user/:username', async (req, res) => {
  const { username } = req.params;
  const { data, error } = await supabase
    .from('users')
    .select('*')
    .eq('username', username)
    .single();
  if (error || !data) return res.status(404).json({ error: 'User not found' });
  res.json(data);
});

// Pi Payment Webhook (called by Pi servers)
app.post('/api/pi/payment', async (req, res) => {
  try {
    const { paymentId, txid } = req.body;
    // Approve payment if not already approved
    const payment = await approvePayment({ paymentId });
    // Mark as completed if txid sent by Pi Network
    if (txid) {
      await completePayment(paymentId, txid);
    }
    // Save record to Supabase
    await supabase.from('payments').upsert([
      {
        payment_id: payment.identifier,
        username: payment.user_uid,
        amount: payment.amount,
        txid: txid || null,
        status: txid ? 'completed' : 'approved'
      }
    ], { onConflict: ['payment_id'] });
    res.json({ ok: true });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// For frontend polling: get payment status by paymentId
app.get('/api/payment/:paymentId', async (req, res) => {
  try {
    const payment = await getPayment(req.params.paymentId);
    res.json({
      payment_id: payment.identifier,
      status: payment.status,
      user_uid: payment.user_uid,
      amount: payment.amount,
      txid: payment.transaction?.txid || null
    });
  } catch (e) {
    res.status(404).json({ error: e.message });
  }
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () =>
  console.log(`Backend running on http://localhost:${PORT}`)
);
