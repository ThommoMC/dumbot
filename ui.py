import discord
import random

games = []
uservoted = []
random.seed()
class GameVote(discord.ui.View):
    async def on_timeout(self):
        self.disable_all_items()
        selectedGame = games[random.randrange(len(games))]
        await self.message.edit(content=f"Times Up! The selected game is: {selectedGame}", view=self)

    @discord.ui.button(label="Vote Here!", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.interactions):
        if interaction.user.id in uservoted:
            await interaction.response.send_message(f"__**{interaction.user} tried to vote twice!**__", delete_after=3600)
            return
        else:
            await interaction.response.send_modal(GameVoteModal(title="Vote for a game!"))
            uservoted.append(interaction.user.id)

class GameVoteModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Enter Game Here!"))

    async def callback(self, interaction):
        games.append(self.children[0].value)
        await interaction.response.send_message(f"{interaction.user} has voted!", delete_after=120)
