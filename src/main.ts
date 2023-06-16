import * as core from '@actions/core'
import * as fs from 'fs'
import * as path from 'path'

async function run(): Promise<void> {
  try {
    const envKeys = Object.keys(process.env).sort((a, b) => a.localeCompare(b))

    let outFile = ''

    for (const key of envKeys) {
      if (key.startsWith('INPUT_ENVKEY_')) {
        const value = process.env[key] || ''

        if (value === '' && core.getInput('fail_on_empty') === 'true') {
          throw new Error(`Empty env key found: ${key}`)
        }

        outFile += `${key.split('INPUT_ENVKEY_')[1]}=${value}\n`
      }
    }

    const directory = core.getInput('directory') || ''
    const fileName = core.getInput('file_name') || '.env'
    let filePath = process.env['GITHUB_WORKSPACE'] || '/github/workspace'

    if (filePath === '' || filePath === 'None') {
      filePath = '.'
    }

    if (directory === '') {
      filePath = path.join(filePath, fileName)
    } else if (directory.startsWith('/')) {
      throw new Error(
        'Absolute paths are not allowed. Please use a relative path.'
      )
    } else if (directory.startsWith('./')) {
      filePath = path.join(filePath, directory.slice(2), fileName)
    } else {
      filePath = path.join(filePath, directory, fileName)
    }

    core.debug(`Creating file: ${filePath}`)

    fs.writeFileSync(filePath, outFile)
  } catch (error) {
    if (error instanceof Error) core.setFailed(error.message)
  }
}

void run()
