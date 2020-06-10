import random
run = True
while run == True:
    question = input("What is the question that you would like to ask the magic eight ball? ")

    options = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
                     'Concentrate and ask again.', 'Don’t count on it. '
                                                   'It is certain.', 'It is decidedly so.', 'Most likely.',
                     'My reply is no.', 'My sources say no.',
                     'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.',
                     'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']

    print(f"Answer: {random.choice(options)}")
