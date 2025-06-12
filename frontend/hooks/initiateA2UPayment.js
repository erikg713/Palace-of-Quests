async function initiateA2UPayment() {
  const amount = 5;
  const memo = "Quest completion reward";
  const metadata = { quest_id: "q123" };
  const uid = user.uid;

  // 1. Create
  const { payment_id } = await fetch("/api/pi/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, memo, metadata, uid })
  }).then(res => res.json());

  // 2. Submit
  const { txid } = await fetch("/api/pi/submit-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ payment_id })
  }).then(res => res.json());

  // 3. Complete
  const { payment } = await fetch("/api/pi/complete-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ payment_id, txid })
  }).then(res => res.json());

  console.log("Payment complete", payment);
}
