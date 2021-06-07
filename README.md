# EVE Online Tweetbot
The [EVE Online](https://www.eveonline.com/) Tweetbot fetchs the current player numbers from the [EVE Swagger Interface](https://esi.evetech.net/ui/#/) - an OpenAPI for the EVE Online game - and sends out a tweet (with a few random stats) using the Twitter API process every 15 minutes (fingers crossed).

EVE Online Tweetbot is a software project written in Python. It was originally started as a way to practice programming in Python and help the author to better understand the game. Whilst it has not helped with the second part, it has been very useful as a practical Python language programming exercise.

It has also been used as a tool for further learning about APIs, general development workflow, authentication, Docker, containers and self-hosting. It is currently running on a Raspberry Pi 2 Model B V1.1. The host system is running [HypriotOS](https://blog.hypriot.com/getting-started-with-docker-on-your-arm-device/).

Follow the Eve Online Tweetbot on [Twitter](https://twitter.com/TranquilitySta3), or just have a look and see what the tweets contain.

## Project Status
This project will see "sporadic" development. It has all of the initial intended features and meets the goals of what I was looking to practice. I want to include some better API connection handling (up/down, what to do if no network connection etc) as well as possibly include some unit tests.

## Installation
Directions TBC

## Dependencies
Built with Python 3.9.2

Packages include:
* requests 2.25.1
* Tweepy 3.10.0

## Contributing
If this project piques your interest, feel free to fork and expand on it. If you would like to contribute, please open an issue to discuss the changes proposed/made.

## Licence
All [EVE Online](https://www.eveonline.com/) related materials remain the property of [CCP Games](https://www.ccpgames.com/).

### EVE Online Tweetbot source code licence
[MIT License](https://spdx.org/licenses/MIT.html)

Copyright (c) [2021] [Ken Livesey]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.