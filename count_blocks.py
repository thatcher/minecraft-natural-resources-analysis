################################################################################
# Walk the blocks in a Minecraft PI world and record the block data,
# id and type. The id is the primary type, eg Wood, while the data is
# while the data is secondary type, eg Birch.
#
# The shape of the world is 256xINFx256 centered around 0, with
#   x in the range [-128,127]
#   y in [-INF,INF]
#   z in the range [-128,127]
#
# The y-plane is what we would think of as up/down.  For our inital survey
# we will assume that y is in a similar range.
from mcpi import minecraft
from mcpi import block

import numpy

import settings


# Connect to a raspberry pi mincraft game instance
world = minecraft.Minecraft.create(
    address=settings.SERVER_ADDRESS,
    port=settings.SERVER_PORT
)

# First thind we want to do is make sure we dont accidentally change the
# world we are measuring.  Now the blocks cant be broken by anybody,
# even players.
world.setting("world_immutable", True)

world.postToChat("Counting Levels")

sample_radius = settings.SAMPLE_RADIUS

def countBlock(x,z,y):
    return world.getBlock(
        x - sample_radius/2,
        y,
        z - sample_radius/2
    )

# This is the level we will begin at and we will
# continue in the direction
y = settings.Y_LEVEL
y_next = settings.Y_DIRECTION
is_all_air = False

while not is_all_air:
    print("Counting Level %s" % y)

    # Reset our storage array
    world_data = numpy.zeros(
        (sample_radius,sample_radius),
        dtype=int
    )
    for x in range(0, sample_radius):
        print "X Slice %s" % x
        for z in range(0, sample_radius):
            world_data[x][z] = countBlock(x,z,y)

    # save the slice for later analysis
    print "Saving Slice %s" % y
    numpy.save('data/world_%s.npy' % y, world_data)

    if not world_data.sum():
        is_all_air = True
        print "Level %s is all air, stopping counting" % y

    y = y + y_next
