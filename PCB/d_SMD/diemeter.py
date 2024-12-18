import pcbnew

# Define the new diameter value (in micrometers)
new_diameter = 1.5  # Change this to your desired diameter

def change_net_diameter(net):
  for track in net.GetTracks():
    track.SetWidth(new_diameter)  # Set width for tracks
  for via in net.GetVias():
    via.SetDrill(new_diameter)  # Set drill size for vias

# Get the board object
board = pcbnew.GetBoard()

# Iterate through al nets in the board
for net in board.GetNets():
  change_net_diameter(net)

# Save the modified board (optional)
# pcbnew.SaveBoard(board, "modified_board.kicad_pcb")

print("Net diameters changed to", new_diameter, "micrometers")

