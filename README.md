# 🤖 Supertelligence Discord Bot

A Discord bot that connects users to an LLM service, allowing them to chat with AI directly in their Discord servers.

## ✨ Features

- 💬 Chat with an AI assistant by mentioning the bot or sending direct messages
- 🚀 FastAPI backend for scalable LLM integration
- 🎯 Automatic message chunking for long responses
- 🔧 Easy configuration with environment variables
- 📱 Modern Discord integration with slash commands

## 🛠️ Setup Instructions

### 1. Prerequisites

- Python 3.13+
- Poetry (for dependency management)
- Discord Developer Account
- OpenAI API Account

### 2. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name (e.g., "Supertelligence")
3. Go to the "Bot" section in the left sidebar
4. Click "Add Bot"
5. Under "Token", click "Copy" to get your bot token
6. Under "Privileged Gateway Intents", enable:
   - ✅ Message Content Intent
   - ✅ Server Members Intent (optional)

### 3. Get OpenAI API Key

1. Go to [OpenAI API](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key for use in your environment file

### 4. Environment Setup

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` with your actual values:
   ```env
   DISCORD_BOT_TOKEN=your_actual_discord_bot_token
   OPENAI_API_KEY=your_actual_openai_api_key
   API_BASE_URL=http://localhost:8000
   ```

### 5. Install Dependencies

```bash
poetry install
```

### 6. Run the Application

```bash
poetry run python src/supertelligence_backend/run.py
```

This will start both the FastAPI backend and Discord bot simultaneously.

### 7. Invite Bot to Your Server

1. Go back to the Discord Developer Portal
2. Navigate to "OAuth2" > "URL Generator"
3. Select scopes:
   - ✅ `bot`
   - ✅ `applications.commands`
4. Select permissions:
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Use Slash Commands
   - ✅ Embed Links
5. Copy the generated URL and open it in your browser
6. Select your Discord server and authorize the bot

## 🎮 How to Use

### Mention the Bot
In any channel where the bot has permissions:
```
@Supertelligence What's the weather like today?
```

### Direct Messages
Send a direct message to the bot:
```
Hello! Can you help me with Python programming?
```

### Commands
- `!ping` - Check if the bot is responsive
- `!help_supertelligence` - Show help information

## 🏗️ Project Structure

```
supertelligence-backend/
├── src/
│   └── supertelligence_backend/
│       ├── __init__.py
│       ├── main.py           # FastAPI application
│       ├── discord_bot.py    # Discord bot implementation
│       └── run.py            # Startup script
├── tests/
├── pyproject.toml           # Poetry configuration
├── env.example              # Environment variables template
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DISCORD_BOT_TOKEN` | Your Discord bot token | ✅ |
| `OPENAI_API_KEY` | Your OpenAI API key | ✅ |
| `API_BASE_URL` | Backend API URL | ❌ (defaults to localhost:8000) |

### Bot Customization

You can customize the bot's behavior by editing `discord_bot.py`:

- Change the system prompt in `main.py`
- Modify the response format
- Add new commands
- Implement user-specific conversation history

## 🚀 Deployment

### Local Development
The current setup is perfect for local development and testing.

### Production Deployment
For production, consider:

1. **Use a proper database** (PostgreSQL, MySQL)
2. **Deploy to cloud platforms** (AWS, GCP, Azure)
3. **Use Docker** for containerization
4. **Set up monitoring** and logging
5. **Configure rate limiting** for the API

## 🐛 Troubleshooting

### Bot doesn't respond
1. Check if the bot is online in your Discord server
2. Verify the bot has permission to read and send messages
3. Ensure Message Content Intent is enabled
4. Check the console for error messages

### API errors
1. Verify your OpenAI API key is valid and has credits
2. Check if the FastAPI server is running on port 8000
3. Look for error messages in the console

### Environment issues
1. Make sure your `.env` file exists and has the correct values
2. Verify all required environment variables are set
3. Check file permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🔮 Future Features

- [ ] Conversation history per user
- [ ] Multiple LLM provider support
- [ ] Slash commands
- [ ] Server-specific configuration
- [ ] Usage analytics
- [ ] Rate limiting per user
- [ ] Custom AI personalities
