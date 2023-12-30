import { readFile } from "fs/promises"
import { join as joinPath } from "path"

export const importFileStrArray = async (
  fileName: string
): Promise<string[]> => {
  return (await readFile(joinPath(process.cwd(), fileName), "utf8"))
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l.length > 0)
}
