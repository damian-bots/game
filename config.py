from utils.enums import PlayerRole


chats = {}

# players
MAX_PLAYERS = 25
MIN_PLAYERS = 5
MIN_PLAYERS_FOR_2_MAFIOSO = 12
MIN_PLAYERS_FOR_3_MAFIOSO = 18


# delays(in seconds)
registration_duration = 60
night_voting_duration = 60
conversation_duration = 60
day_voting_duration = 20

# bot messages
greetings = {PlayerRole.MAFIOSO : f'You are *{PlayerRole.MAFIOSO}*\.\n'\
                                   'Your main goal is to eliminate innocents\.\n'\
                                   "Good luck and don't let other players guess who you are\!",
            PlayerRole.INNOCENT:  f'You are *{PlayerRole.INNOCENT}*\.\n'\
                                   "There's not much you can do to stop mafia\,\n"\
                                   'but if you cooperate with other innocents your city might stand a chance\.',
            PlayerRole.DETECTIVE: f'You are *{PlayerRole.DETECTIVE}*\,\n'\
                                   "the only hope of this city in fight against mafia\.\n"\
                                   'Good luck\!',
            PlayerRole.DOCTOR:    f'You are *{PlayerRole.DOCTOR}*\,\n'\
                                   'you can heal players killed during the night\.\n'\
                                   "Beware of helping mafia and also don't be too selfish\!"}

help_message = 'Hi there, I am *Mafia Bot*\n'\
               'I understand theese commands:\n'\
               '• /help \- display this help message\n'\
               '• /start \- start registration\n'\
               '• /begin \- finish registration and start game\n'\
               '• /stop \- stop game\n'\
               '♣︎ 𝗢𝘄𝗻𝗲𝗿 - @its_damiann'\

# starting the game
game_start_message = 'Starting new game\!'
game_in_progress_message = 'Game is already in progress'
game_private_message = "You can't play alone, can you?"
no_active_registration_message = 'There is no active registration in this chat'

# stopping the game
game_idle_message = 'Game is not running, nothing to stop'
game_stopped_message = 'Stopped the game'
not_enough_players_message = 'Not enough players, game will not begin'

# registration
successfull_registration_message = 'You have successfully registered!'
early_registration_message = 'Unable to register, start game first'
late_registration_message = 'Too late, wait for current game to stop'
double_registration_message = 'You are already registered'
registration_error_message = 'An error occured, please retry'

# during the game
game_begins_message = 'The game begins!'
conversation_message = f'You now have *{conversation_duration} seconds* to discuss the situation'
day_vote_message = f"It's time to lynch mafia, you've got *{day_voting_duration} seconds* to make your choice"
voting_time_expired_message = 'Voting time expired'
