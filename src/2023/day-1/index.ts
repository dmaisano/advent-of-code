import { readFile } from "fs/promises"
import { join as joinPath } from "path"
import { importFileStrArray } from "../utils"

const digitMap: {
  [key: string]: string
} = {
  zero: "0",
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
}
const digitMapEntries = Object.entries(digitMap)

function isDigit(char: string): boolean {
  return /^\d$/.test(char)
}

function getCalibrationValue(line: string): number {
  const digits: string[] = []

  for (let i = 0; i < line.length; i++) {
    const char = line[i] ?? ""

    if (isDigit(char)) {
      digits.push(char)
      continue
    }

    const subStr = line.substring(i)
    for (const [key, value] of digitMapEntries) {
      if (subStr.startsWith(key)) {
        digits.push(value)
        break
      }
    }
  }

  const firstDigit = digits[0] ?? ""
  const lastDigit = digits[digits.length - 1] ?? ""
  return parseInt(firstDigit + lastDigit)
}

async function main() {
  const lines = await importFileStrArray("./input.txt")

  let sum = 0
  for (const line of lines) {
    sum += getCalibrationValue(line)
  }

  console.log(`The sum of all of the calibration values is: ${sum}`)
  return sum
}

main().catch(console.error)
