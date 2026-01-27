Random dice = new Random();
//#date and time down to the fraction of a millisecond and use that to seed an algorithm that produces a different number each time. 
int roll = dice.Next(1, 7);
Console.WriteLine(roll);