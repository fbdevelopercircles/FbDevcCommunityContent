const express = require('express'),
bodyParser = require('body-parser'),
rp = require('request-promise'),
request = require('request'),
path = require("path");
require('dotenv').config();

app = express();
app.use(bodyParser.json());

// Whitelist the domain Name
var request_body;
// Create a request Body.
request_body = {
  "whitelisted_domains": [`${process.env.URL}`]
}
  // Send the request after setting up the request_body.
    var options = {
      method: 'POST',
      uri: `https://graph.facebook.com/v7.0/me/messenger_profile?access_token=${process.env.PAGE_ACCESS_TOKEN}`,
      body: request_body,
      json: true
    };
    try{
        rp(options);
    } catch (e){
        console.log(e);
    }

// Setting the Callback URL.
request(
    {
      uri: `https://graph.facebook.com/v7.0/${process.env.APP_ID}/subscriptions`,
      qs: {
        access_token: `${process.env.APP_ID}|${process.env.APP_SECRET}`,
        object: "page",
        callback_url: `${process.env.URL}/webhook`,
        verify_token: process.env.VERIFY_TOKEN,
        fields: "messages, messaging_postbacks, messaging_optins, message_deliveries",
        include_values: "true"
      },
      method: "POST"
    },
    (error, _res, body) => {
      if (!error) {
        console.log("Callback URL:", body);
      } else {
        console.error("Callback URL have issues:", error);
      }
    }
  );

// Webhook Endpoint
app.post('/webhook', (req, res) => {  
    let body = req.body;
    // Checks this is an event from a page subscription
    if (body.object === 'page') {
      // Iterates over each entry - there may be multiple if batched
      body.entry.forEach(function(entry) {
      // Gets the body of the webhook event
      if(entry.messaging){
        webhook_event = entry.messaging[0];
        // Get the sender PSID
        let sender_psid = webhook_event.sender.id;

        // If optins like "OTN"
        if (webhook_event.optin){
            console.log(webhook_event);
        }

        if(webhook_event.message && sender_psid !== `${process.env.PAGE_ID}` && !webhook_event.message.quick_reply){
            hanldeMessages(sender_psid, webhook_event);
        } else if (webhook_event.postback || (webhook_event.message && webhook_event.message.quick_reply)){
            hanldePostback(sender_psid, webhook_event);
        }
    }
    });
    // Returns a '200 OK' response to all requests
    res.status(200).send('EVENT_RECEIVED');
    } else {
        // Returns a '404 Not Found' if event is not from a page subscription
        res.sendStatus(404);
      }
    });

// Adds support for GET requests to our webhook
app.get('/webhook', (req, res) => {    
    // Parse the query params
    let mode = req.query['hub.mode'];
    let token = req.query['hub.verify_token'];
    let challenge = req.query['hub.challenge'];      
    // Checks if a token and mode is in the query string of the request
    if (mode && token) {
      // Checks the mode and token sent is correct
      if (mode === 'subscribe' && token === process.env.VERIFY_TOKEN) {   
        // Responds with the challenge token from the request
        console.log('WEBHOOK_VERIFIED');
        res.status(200).send(challenge);  
      } else {
      // Responds with '403 Forbidden' if verify tokens do not match
      res.sendStatus(403);      
      }
    }
  });


// Handle Messages
function hanldeMessages(sender_psid, webhook_event){
    // You can Check for Specific Text and send other response.
    console.log(webhook_event);
    response = {"text":`You sent Text Message '${webhook_event.message.text}'`};
    callSendAPI(sender_psid, response);
}

// Handle Postbacks
function hanldePostback(sender_psid, webhook_event){
    // You can Check for Specific Postback and send other response.
    console.log(webhook_event);
    response = {"text":`You sent Text Message '${webhook_event.postback.title}'`};
    callSendAPI(sender_psid, response);
}

// Call Send API Function
function callSendAPI(sender_psid, response){
    token = process.env.PAGE_ACCESS_TOKEN;
    persona_id = null;
    request_body = {
        "recipient": {
        "id": sender_psid
        },
        "message": response,
        "persona_id":persona_id
    }
    var options = {
        method: 'POST',
        uri: `https://graph.facebook.com/v7.0/me/messages?access_token=${token}`,
        body: request_body,
        json: true
    };
    rp(options);
    console.log("sent");
}

// listen for webhook events //
app.listen(process.env.PORT || 3370, () => console.log('webhook is listening'));
