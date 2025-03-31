const {Client, GatewayIntentBits, Partials} = require('discord.js');
const { configDotenv } = require('dotenv');
const fs = require('node:fs');
const e = require('node:child_process');

configDotenv()

const client = new Client({ intents: [ 
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent],
    partials: [Partials.Message, Partials.Channel],
});

client.on('ready', client => {
    console.log("Hello console!");
    //client.channels.cache.get('595676109845037060').send('Hello here!');
    sleepThenAct()
})

client.login(process.env.token);

function sleepFor(sleepDuration){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration) {}
}

function sleepThenAct(){
    e.exec("python ../scraper.py > out.txt", (error, stdout, stderr) => {
        if (error) {
            console.error(`error: ${error.message}`);
            return;
          }
        
          if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
          }
        
          console.log(`stdout:\n${stdout}`);
    });
    lines = fs.readFileSync('./out.txt').toString().split('\n');
    for (i = 0; i < lines.length; i++) {
        lines[i]
    }
    while (true) {
        console.log("Hello, JavaScript sleep!");
        sleepFor(1000);
    }
}