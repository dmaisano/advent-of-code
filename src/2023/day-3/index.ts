import { importFileStrArray } from "../utils"

type Symbol = "*" | "#" | "+" | "$"

function part1Soln(lines: string[]) {
  let result = 0
  for (let i = 0; i < lines.length; i++) {
    const numbers = lines[i].replace(/\./g, " ")
    for (const match of numbers.matchAll(/\d+/g)) {
      for (let j = match.index; j < match.index + match[0].length; j++) {
        const surrounding = [
          (lines[i - 1] ?? "")[j - 1] ?? ".",
          (lines[i - 1] ?? "")[j] ?? ".",
          (lines[i - 1] ?? "")[j + 1] ?? ".",
          (lines[i] ?? "")[j - 1] ?? ".",
          (lines[i] ?? "")[j] ?? ".",
          (lines[i] ?? "")[j + 1] ?? ".",
          (lines[i + 1] ?? "")[j - 1] ?? ".",
          (lines[i + 1] ?? "")[j] ?? ".",
          (lines[i + 1] ?? "")[j + 1] ?? ".",
        ]
        if (surrounding.some((x) => /[^0-9.]/.test(x))) {
          result += parseInt(match[0])
          break
        }
      }
    }
  }
  return result
}

async function main({ debug }: { debug: boolean } = { debug: false }) {
  const lines = await importFileStrArray(
    "./input.txt",
    debug && [
      "467..114..",
      "...*......",
      "..35..633.",
      "......#...",
      "617*......",
      ".....+.58.",
      "..592.....",
      "......755.",
      "...$.*....",
      ".664.598..",
    ]
  )
  // const schematic = lines.map((row) => row.split(""))

  const sumOfNumbers = part1Soln(lines)
  console.log(
    `Sum of all of the part numbers in the engine schematic: ${sumOfNumbers}`
  )
  return sumOfNumbers
}

main({ debug: false }).catch(console.error)
