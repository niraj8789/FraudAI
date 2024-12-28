const plaid = require('plaid');  // Import the Plaid module

const handler = plaid.create({
    token: 'link-sandbox-d7a248cf-0db0-4b22-bf3a-8b0d1d9fbb20', // Replace with your link token
    onSuccess: function(public_token, metadata) {
        console.log('Public Token: ', public_token);
    },
});

handler.open();
