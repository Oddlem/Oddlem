Hi! This is my first ACTUAL python project, wherein I needed to code everything from scratch! This means I didn't use any tutorials, this was me and some syntax help from friends.

Because this was entirely from scratch, you might notice that this looks pretty messy. Luckily, I'm planning on continuously updating this which I hope will show my improvement! 

The last step is to add images and make it look better. For now, the code itself is the focus!

For now, I just wanted to create something. And that something has a bit of inefficient code. My next step is to become better at functions, and streamline things to be better in the background!

From the user's end, the process goes like this:
1. Enter Start, to trigger the quiz to start. If you say anything else, it'll insist the user to say "Start".
2. The quiz starts, the first question is asked. From there, until the 10th question, the user will answer them.
3. Finally, the game gives you a score... your toughness score!


Now, from the actual code's end, I'll explain my reasoning a little:
1. I defined variables, key ones being "userscore", "rightanswer(1,2,3,4)", and "quizanswers". 

   a. It doesn't seem like much at first, but quizanswers is what allows the quiz to run smoothly in the scenario that a user says something else; it allows ONLY numbers 1-4 to be answers!

   b. Userscore starts from 0 and, if you get a right answer, will trigger a counter to go off which will add ONLY under this condition. This gives your toughness score at the end! This I plan on turning into a function

   c. The "rightanswer" variables are a part of syntax of this trigger going off. I also hope to streamline these as well in the future!
3. Using a while loop, I made it so that the user NEEDS to specifically say "Start". Once they do, the "test giver" announces this and the loop breaks-- I did it this way to make it more clear what's happening!
4. I then made each question using while loops. Although inefficient and I'm sure there's a better way, I did it this way for the sake of using "continue" under the pretense that the user gives an invalid answer. I didn't want it to simply move onto the next question in case there's an input mistake, so I decided to make a loop under the assumption that this COULD happen. So, the user is "stuck" until they enter a valid answer. 

    a. IF the answer is valid (meaning it's a number 1-4), AND it also happens to be a "rightanswer", it will trigger a smaller loop to trigger that will cause "userscore" to tick upward.
   
6. Finally, after question 10, the loop breaks and it triggers a "score" loop. I made 6 different possible outcomes based on the score, and the score can only meet one condition. So, let's say you got 50% right, it will check each loop for the single elif statement it can apply to and, once it finds it, the loop breaks and it prints the message correlating to the percentage it's closest to.
