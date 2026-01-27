Random dice = new Random();
//#date and time down to the fraction of a millisecond and use that to seed an algorithm that produces a different number each time. 
int roll1 = dice.Next();
int roll2 = dice.Next(101);
int roll3 = dice.Next(50, 101);

Console.WriteLine($"First roll: {roll1}");
Console.WriteLine($"Second roll: {roll2}");
Console.WriteLine($"Third roll: {roll3}");