import units.player
import locations.start

class EventLoop():
  def run(self):
    player = units.player.Player("Player", 10)
    player.location = locations.start.Start()

    while player.is_alive:
      player.location.update_unit(player)
      player.turn_ended = False

      while player.is_alive and not player.turn_ended:
        cmd_input = input("C:\>").lower()
        valid = False
        for command in player.location.available_commands():
          if cmd_input == command.name:
            valid = True
            player.execute_command(command, **command.kwargs)
            break
        if not valid == True:
          print("{} is not a valid action.".format(cmd_input))

    print("You died.")
