import scripts.utils as utils

# setup the model and other dependencies
setup = utils.Setup()

# data to test on
test_data = """Ever watched a movie that lost the plot?
Well, this didn't even really have one to begin with. Where to begin?
The achingly tedious scenes of our heroine sitting around the house with actually
no sense of menace or even foreboding created even during the apparently constant
thunderstorms (that are strangely never actually heard in the house-great double glazing)?
The house that is apparently only a few miles from a town yet is several hours walk away(?)
or the third girl who serves no purpose to the plot except to provide a surprisingly quick
gory murder just as the tedium becomes unbearable? Or even the beginning which suggests
a spate of 20+ killings throughout the area even though it is apparent the killer never
ventures far from the house? Or the bizarre ritual with the salt & pepper that pretty much
sums up most of the films inherent lack of direction. Add a lead actress who can't act but
at least is willing to do some completely irrelevant nude shower scenes and this video
is truly nasty, but not in the way you hope. Given a following simply for being banned
in the UK in the 80's (mostly because of a final surprisingly over extended murder)
it offers nothing but curiosity value- and one classic 'daft' murder
(don't worry-its telegraphed at least ten minutes before). After a walk in the woods
our victim comes to a rather steep upward slope which they obviously struggle up.
Halfway through they see a figure at the top dressed in black and brandishing a large scythe.
What do they do? Slide down and run like the rest of us? No, of course not-
they struggle to the top and stand conveniently nice and upright in front of the murder weapon.
It really IS only a movie as they say.."""

# make predictions
result = setup.predict(test_data)
# print result
print(result)
