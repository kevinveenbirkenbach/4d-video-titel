# 4D Video Titel (4dvt) 🎬🌍⏰
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/kevinveenbirkenbach/4dvt.svg?style=social)](https://github.com/kevinveenbirkenbach/4dvt/stargazers)

4D Video Titel is a command-line tool that generates descriptive titles for video files by extracting geolocation and timestamp metadata. Using ffprobe, it retrieves GPS data and creation time from videos, automatically determines the local timezone based on the GPS coordinates, and then formats a title that includes a custom prefix, the localized date and time, and the GPS coordinates. This gives your video titles a four-dimensional perspective—combining space and time.

## 🛠 Features

- **Metadata Extraction:** Uses ffprobe to extract video metadata including creation time and GPS location.
- **Timezone Conversion:** Automatically converts UTC creation time to local time using GPS data.
- **Custom Title Generation:** Formats titles as `<prefix> <YYYY-MM-DDTHH:MM>-<timezone>, <longitude>°, <latitude>°`.
- **Multi-Format Support:** Works with various video formats (e.g., .mp4, .mov, .avi, .mkv).
- **Easy Integration:** Operates as a simple CLI tool that fits seamlessly into your workflow.

## 📥 Installation

Install 4D Video Titel via [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager) under the alias `4dvt`:

```bash
package-manager install 4dvt
```

This command installs the tool globally, making it available as `4dvt` in your terminal. 🚀

## 🚀 Usage

Run 4D Video Titel by specifying the directory containing your video files and a custom prefix for the titles:

```bash
4dvt /path/to/video/directory "My Video Prefix"
```

The tool will traverse the specified directory, extract the necessary metadata from each video, and print the generated title for each file.

## 🧑‍💻 Author

Developed by **Kevin Veen-Birkenbach**  
- 📧 [kevin@veen.world](mailto:kevin@veen.world)  
- 🌐 [https://www.veen.world](https://www.veen.world)

## 📜 License

This project is licensed under the **MIT License**.

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues to help improve 4D Video Titel. Let's create meaningful video titles together! 😊
