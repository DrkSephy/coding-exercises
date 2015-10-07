function tug_o_war(teams) {
  //Code
  var team1 = teams[0].reduce((a, b) => a + b);
  var team2 = teams[1].reduce((a, b) => a + b);
   
  if (team1 > team2) {
    return "Team 1 wins!";
  }
  
  else if (team1 < team2) {
    return "Team 2 wins!";
  }
  
  else {
    return "It's a tie!";
  }
}