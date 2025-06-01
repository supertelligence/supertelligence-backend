import discord
from discord.ext import commands
import aiohttp
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Bot configuration
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Bot permissions and intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has landed! Connected to Discord.')
    print(f'Bot is in {len(bot.guilds)} servers')
    
    # Set bot activity
    activity = discord.Activity(type=discord.ActivityType.listening, name="your messages | Type @Supertelligence to chat!")
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    # Don't respond to our own messages
    if message.author == bot.user:
        return
    
    # Check if the bot is mentioned or if it's a DM
    is_mentioned = bot.user in message.mentions
    is_dm = isinstance(message.channel, discord.DMChannel)
    
    if is_mentioned or is_dm:
        # Remove the mention from the message content
        content = message.content
        if is_mentioned:
            content = content.replace(f'<@{bot.user.id}>', '').strip()
            content = content.replace(f'<@!{bot.user.id}>', '').strip()
        
        if not content:
            await message.reply("Hello! Ask me anything, and I'll help you out! 🤖")
            return
        
        # Show typing indicator
        async with message.channel.typing():
            try:
                # Send request to FastAPI backend
                async with aiohttp.ClientSession() as session:
                    payload = {
                        "message": content,
                        "user_id": str(message.author.id),
                        "username": message.author.display_name
                    }
                    
                    async with session.post(f"{API_BASE_URL}/chat", json=payload) as response:
                        if response.status == 200:
                            data = await response.json()
                            ai_response = data["response"]
                            
                            # Discord has a 2000 character limit for messages
                            if len(ai_response) > 2000:
                                # Split the response into chunks
                                chunks = [ai_response[i:i+2000] for i in range(0, len(ai_response), 2000)]
                                for chunk in chunks:
                                    await message.reply(chunk)
                            else:
                                await message.reply(ai_response)
                        else:
                            await message.reply("Sorry, I'm having trouble thinking right now. Please try again later! 🤔")
                            
            except Exception as e:
                print(f"Error processing message: {e}")
                await message.reply("Oops! Something went wrong. Please try again later! 😅")
    
    # Process other commands
    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    """Check if the bot is responsive"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Latency: {latency}ms')

@bot.command(name='help_supertelligence')
async def help_command(ctx):
    """Show help information"""
    embed = discord.Embed(
        title="Supertelligence Bot Help",
        description="I'm an AI assistant that can help you with questions and conversations!",
        color=0x00ff00
    )
    
    embed.add_field(
        name="How to talk to me:",
        value="• Mention me (@Supertelligence) in any channel\n• Send me a direct message\n• Use `!ping` to check if I'm online",
        inline=False
    )
    
    embed.add_field(
        name="What I can do:",
        value="• Answer questions\n• Have conversations\n• Help with various topics\n• Provide information and explanations",
        inline=False
    )
    
    await ctx.send(embed=embed)

async def main():
    """Main function to run the bot"""
    if not DISCORD_TOKEN:
        print("ERROR: DISCORD_BOT_TOKEN not found in environment variables!")
        return
    
    try:
        await bot.start(DISCORD_TOKEN)
    except discord.LoginFailure:
        print("ERROR: Invalid Discord bot token!")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 