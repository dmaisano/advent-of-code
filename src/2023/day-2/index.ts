import { importFileStrArray } from "../utils"

type Game = {
  id: number
  counts: { red: number; green: number; blue: number }[]
}

function parseGame(s: string): Game {
  const [idPart, ...countParts] = s.split(": ")
  const id = parseInt(idPart.replace("Game ", ""), 10)
  const counts = countParts
    .join(": ")
    .split("; ")
    .map((part) => {
      const colors = { red: 0, green: 0, blue: 0 }
      part.split(", ").forEach((colorPart) => {
        const [count, color] = colorPart.split(" ")
        colors[color as "red" | "green" | "blue"] = parseInt(count, 10)
      })
      return colors
    })
  return { id, counts }
}

// function isGamePossible(
//   game: Game,
//   maxCounts: { red: number; green: number; blue: number }
// ): boolean {
//   return game.counts.every(
//     (counts) =>
//       counts.red <= maxCounts.red &&
//       counts.green <= maxCounts.green &&
//       counts.blue <= maxCounts.blue
//   )
// }

// function sumPossibleGameIds(
//   games: string[],
//   maxCounts: { red: number; green: number; blue: number }
// ): number {
//   return games
//     .map(parseGame)
//     .filter((game) => isGamePossible(game, maxCounts))
//     .reduce((sum, game) => sum + game.id, 0)
// }

function minCubesForGame(game: Game): {
  red: number
  green: number
  blue: number
} {
  return game.counts.reduce(
    (minCounts, counts) => ({
      red: Math.max(minCounts.red, counts.red),
      green: Math.max(minCounts.green, counts.green),
      blue: Math.max(minCounts.blue, counts.blue),
    }),
    { red: 0, green: 0, blue: 0 }
  )
}

function powerOfSet(set: { red: number; green: number; blue: number }): number {
  return set.red * set.green * set.blue
}

function sumPowersOfMinSets(games: string[]): number {
  return games
    .map(parseGame)
    .map(minCubesForGame)
    .map(powerOfSet)
    .reduce((sum, power) => sum + power, 0)
}

async function main({ debug }: { debug: boolean } = { debug: false }) {
  const games: string[] = await importFileStrArray(
    "./input.txt",
    debug && [
      "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
  )

  const maxCounts = { red: 12, green: 13, blue: 14 }
  const solution = sumPowersOfMinSets(games)
  console.log(`Sum of IDs of possible games: ${solution}`)
  return solution
}

main({ debug: false }).catch(console.error)
