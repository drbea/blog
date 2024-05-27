const fs = require('fs');
const path = require('path');

const srcDir = path.join(__dirname, 'node_modules', 'bootstrap', 'dist');
const destDir = path.join(__dirname, 'static');

if (!fs.existsSync(destDir)) {
    fs.mkdirSync(destDir, { recursive: true });
}

fs.readdirSync(srcDir).forEach(dir => {
    const srcPath = path.join(srcDir, dir);
    const destPath = path.join(destDir, dir);

    fs.cpSync(srcPath, destPath, { recursive: true });
});
