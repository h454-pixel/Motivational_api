from fastapi import APIRouter

router = APIRouter()

@router.get("/goals")
def get_goal_quote():

    return {
            "quotes": [
                "Success is the sum of small efforts, repeated day in and day out.",
                "Believe you can and you're halfway there.",
                "Dream big, work hard, stay focused.",
                "Small progress is still progress.",
                "Your only limit is your mind.",
                "Discipline is the bridge between goals and accomplishment.",
                "Great things never come from comfort zones.",
                "Every day is a new opportunity to improve.",
                "Do something today that your future self will thank you for.",
                "Success starts with the decision to try.",
                "Stay focused and never give up.",
                "Your future is created by what you do today.",
                "One step at a time is still moving forward.",
                "Don't stop until you're proud.",
                "Consistency beats motivation.",
                "You are capable of more than you think.",
                "Make yourself proud.",
                "Focus on the goal, not the obstacles.",
                "Hard work creates opportunities.",
                "Progress takes patience.",
                "Keep going. Your effort will pay off.",
                "Turn your dreams into plans.",
                "Action is the key to success.",
                "Be stronger than your excuses.",
                "A little progress each day adds up to big results.",
                "Success requires patience and persistence.",
                "Your goals are worth the effort.",
                "Stay patient. Stay consistent. Stay focused.",
                "Difficult roads often lead to beautiful destinations.",
                "Start where you are. Use what you have. Do what you can.",
                "Don't wait for opportunity. Create it.",
                "Your determination will take you further than talent alone.",
                "Focus on becoming better, not being perfect.",
                "Every achievement begins with the decision to try.",
                "Work hard in silence. Let your success make the noise.",
                "Keep your eyes on the goal and your feet moving.",
                "Nothing changes if nothing changes.",
                "You don't have to be great to start, but you have to start.",
                "Make today count.",
                "Believe in your journey.",
                "Success is built one day at a time.",
                "Never underestimate the power of consistency.",
                "Push yourself because no one else will do it for you.",
                "Your effort today shapes your tomorrow.",
                "Stay committed to your goals.",
                "Don't quit when it gets hard. Keep moving.",
                "The best time to start is now.",
                "Your mindset determines your direction.",
                "Keep chasing the person you want to become.",
                "You are one decision away from a different future."
            ]
        }