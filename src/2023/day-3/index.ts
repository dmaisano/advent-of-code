import path from "path"
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

function part2Soln(lines: string[]) {
  const resultArray: string[] = []

  const numberIndices = []
  for (let i = 0; i < lines.length; i++) {
    const numbers = lines[i].replace(/\./g, " ")

    for (const match of numbers.matchAll(/\*/g)) {
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
        const indices = [
          [i - 1, j - 1],
          [i - 1, j],
          [i - 1, j + 1],
          [i, j - 1],
          [i, j],
          [i, j + 1],
          [i + 1, j - 1],
          [i + 1, j],
          [i + 1, j + 1],
        ]
        const localNumberIndices = []
        for (let k = 0; k < surrounding.length; k++) {
          if (
            /\d/.test(surrounding[k]) &&
            (!/\d/.test(surrounding[k - 1] ?? "") || k % 3 == 0)
          )
            localNumberIndices.push(indices[k])
        }
        if (localNumberIndices.length == 2)
          numberIndices.push(...localNumberIndices)
      }
    }
  }

  for (const index of numberIndices) {
    const [i, j] = index
    const line = lines[i]
    const num = ["", "", "", line[j], "", "", ""]
    if (/\d/.test(line[j - 1] ?? "")) num[2] = line[j - 1]
    if (num[2] != "" && /\d/.test(line[j - 2] ?? "")) num[1] = line[j - 2]
    if (num[1] != "" && /\d/.test(line[j - 3] ?? "")) num[0] = line[j - 3]
    if (/\d/.test(line[j + 1] ?? "")) num[4] = line[j + 1]
    if (num[4] != "" && /\d/.test(line[j + 2] ?? "")) num[5] = line[j + 2]
    if (num[5] != "" && /\d/.test(line[j + 3] ?? "")) num[6] = line[j + 3]
    resultArray.push(num.join(""))
  }
  return resultArray.reduce(
    (a, x, i, r) => a + (i % 2 == 0 ? parseInt(x) * parseInt(r[i + 1]) : 0),
    0
  )
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

  const sumOfNumbers = part2Soln(lines)
  console.log(
    `Sum of all of the part numbers in the engine schematic: ${sumOfNumbers}`
  )
  return sumOfNumbers
}

main({ debug: false }).catch(console.error)
