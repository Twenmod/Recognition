#Time in ~seconds to wait after playing music to be able to play again.
timeout_time = 5

#Duration in ~seconds a face has to be on screen to be fully recognised
hold_duration = 1

#Treshold for how good of a match the face needs to be to be accepted, lower values means it requires more exact matches. Value is ranged 0-1
face_treshold = 0.5

#File locations of all images of faces
known_face_images = [
    "./images/john.jpeg",
    "./images/vsauce.jpeg",
    "./images/sans.jpeg" # Just testing if it would work for ~non human faces (it works decently but not good)
]
#Names of those faces
known_face_names = [
    "John cena",
    "Michael Stevens",
    "Sans undertale"
]
#File locations of music that plays when face is visible
known_face_music = [
    "./sounds/john.mp3",
    "./sounds/vsauce.mp3",
    "./sounds/badtime.mp3"
]