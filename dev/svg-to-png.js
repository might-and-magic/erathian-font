const sharp = require('sharp')

const fs = require('fs')

const pngHeight = 50

const svgDir = './svg-var-width/'
const pngDir = './png/'
if (!fs.existsSync(pngDir)){
	fs.mkdirSync(pngDir)
}

fs.readdirSync(svgDir).forEach(fileName => {
	let char = String.fromCharCode(parseInt(fileName.split('_')[0]))
	let outputFileName;
	if (/[A-Z]/.test(char)) {
		outputFileName = char.toLowerCase() + '_upper.png'
	} else if (/[a-z]/.test(char)) {
		outputFileName = char + '.png'
	}
	if (outputFileName) {
		sharp(svgDir + fileName).resize({ height: pngHeight }).toFile(pngDir + outputFileName)
	}
})
