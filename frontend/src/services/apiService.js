import axios from 'axios';

const apiService = {
    completeQuest: async (userId, paymentId) => {
        try {
            const response = await axios.post('/quests/complete', {
                user_id: userId,
                payment_id: paymentId,
            });
            return response.data;
        } catch (error) {
            console.error("Quest completion failed", error);
            return { error: error.message };
        }
    }
};

export default apiService;

