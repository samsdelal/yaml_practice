import yaml


def yaml_loader(func):
    def wrapped(*args):
        quiw = func(*args)
        with open('test.yaml', 'w') as f:
            yaml.dump(quiw, f, default_flow_style=False)
        return quiw
    return wrapped



some_body = ['Somebody', 'once', 'told', 'me', 'the', 'world', 'is', 'gonna', 'roll', 'me', 'I', "ain't", 'the',
             'sharpest', 'tool', 'in', 'the', 'shed', 'She', 'was', 'looking', 'kind', 'of', 'dumb', 'with', 'her',
             'finger', 'and', 'her']

track = ["Hey now, you're an all star", 'Get your game on, go play', "Hey now, you're a rock star",
         'Get the show on, get paid', 'And all that glitters is gold', 'Only shooting stars break the mold',
         "It's a cool place, and they say it gets colder", "You're bundled up now, wait 'til you get older",
         'But the meteor men beg to differ', 'Judging by the hole in the satellite picture',
         'The ice we skate is getting pretty thin', "The water's getting warm so you might as well swim",
         "My world's on fire, how 'bout yours?", "That's the way I like it and I'll never get bored"]

go = ["Well, the years start coming and they don't stop coming", 'Fed to the rules and I hit the ground running',
      "Didn't make sense not to live for fun", 'Your brain gets smart but your head gets dumb',
      'So much to do, so much to see', "So what's wrong with taking the backstreets?",
      "You'll never know if you don't go (go!)", "You'll never shine if you don't glow"]


@yaml_loader
def get_list(*args):
    return args


print(get_list(some_body, track, go))
