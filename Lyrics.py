class Lyrics(object):

    def __init__(self, title, lyrics):
        self.title = title
        self.lyrics = lyrics
    
    def print_lyrics(self):
        print(f"Title:\t{self.title}\nLyrics:\n{self.lyrics}")


title = "Sultans of Swing"
lyrics = """You get a shiver in the dark
It's raining in the park but meantime
South of the river you stop and you hold everything
A band is blowing Dixie double four time
You feel alright when you hear that music ring

Well, now you step inside but you don't see too many faces
Coming in out of the rain to hear the jazz go down
Competition in other places
Oh, but the horns, they're blowing that sound
Way on down south, way on down south London town

You check out guitar, George
He knows all the chords
Mind it's strictly rhythm
He doesn't wanna make it cry or sing
Left-handed old guitar is all he can afford
When he gets up under the lights to play his thing

And Harry doesn't mind if he doesn't make the scene
He's got a daytime job, he's doing alright
He can play the honky tonk like anything
Saving it up for Friday night
With the Sultans, with the Sultans of Swing

And a crowd of young boys, they're fooling around in the corner
Drunk and dressed in their best brown baggies and their platform soles
They don't give a damn about any trumpet-playing band
It ain't what they call "Rock 'n' Roll"
And the Sultans, yeah, the Sultans, they play Creole, Creole

And then the man, he steps right up to the microphone
And says at last just as the time bell rings
"Goodnight, now it's time to go home."
Then he makes it fast with one more thing,
"We are the Sultans, we are the Sultans of Swing."""

sultans_of_swing_by_Dire_Straits = Lyrics(title, lyrics)
sultans_of_swing_by_Dire_Straits.print_lyrics()
