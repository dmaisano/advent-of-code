import { readFile } from "fs/promises"
import path from "path"

export const importFileStrArray = async (
  filePath: string,
  stub: string[] = []
): Promise<string[]> => {
  if (stub?.length > 0) return stub

  filePath = path.join(path.resolve(process.argv[1], ".."), filePath)
  return (await readFile(filePath, "utf8"))
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l.length > 0)
}
