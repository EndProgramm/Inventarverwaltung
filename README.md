# Inventarverwaltung
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDUuMzQiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAyNDUuMzQgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxODYuMTMiIGhlaWdodD0iMzUiIGZpbGw9IiM4RkM5NjUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxODQuMTMiIHk9IjAiIHdpZHRoPSI2MS4yMTAwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzNSIgZmlsbD0iIzQxOUI1QSIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9Ik0xMy43OCAxOS40MkwxMy43OCAxOS40MkwxNS4yNyAxOS40MlExNS4yNyAyMC4xNSAxNS43NSAyMC41NVExNi4yMyAyMC45NSAxNy4xMiAyMC45NUwxNy4xMiAyMC45NVExNy45MCAyMC45NSAxOC4yOSAyMC42M1ExOC42OCAyMC4zMiAxOC42OCAxOS44MEwxOC42OCAxOS44MFExOC42OCAxOS4yNCAxOC4yOCAxOC45NFExNy44OSAxOC42MyAxNi44NSAxOC4zMlExNS44MiAxOC4wMSAxNS4yMSAxNy42M0wxNS4yMSAxNy42M1ExNC4wNSAxNi45MCAxNC4wNSAxNS43MkwxNC4wNSAxNS43MlExNC4wNSAxNC42OSAxNC44OSAxNC4wMlExNS43MyAxMy4zNSAxNy4wNyAxMy4zNUwxNy4wNyAxMy4zNVExNy45NiAxMy4zNSAxOC42NiAxMy42OFExOS4zNiAxNC4wMSAxOS43NSAxNC42MVEyMC4xNSAxNS4yMiAyMC4xNSAxNS45NkwyMC4xNSAxNS45NkwxOC42OCAxNS45NlExOC42OCAxNS4yOSAxOC4yNiAxNC45MVExNy44NCAxNC41NCAxNy4wNiAxNC41NEwxNy4wNiAxNC41NFExNi4zMyAxNC41NCAxNS45MyAxNC44NVExNS41MyAxNS4xNiAxNS41MyAxNS43MUwxNS41MyAxNS43MVExNS41MyAxNi4xOCAxNS45NiAxNi41MFExNi40MCAxNi44MSAxNy4zOSAxNy4xMFExOC4zOSAxNy40MCAxOC45OSAxNy43OFExOS42MCAxOC4xNiAxOS44OCAxOC42NVEyMC4xNiAxOS4xMyAyMC4xNiAxOS43OUwyMC4xNiAxOS43OVEyMC4xNiAyMC44NiAxOS4zNCAyMS40OVExOC41MiAyMi4xMiAxNy4xMiAyMi4xMkwxNy4xMiAyMi4xMlExNi4yMCAyMi4xMiAxNS40MiAyMS43N1ExNC42NCAyMS40MyAxNC4yMSAyMC44M1ExMy43OCAyMC4yMiAxMy43OCAxOS40MlpNMjQuMTggMTguMTlMMjQuMTggMTguMTlMMjQuMTggMTcuMzlRMjQuMTggMTYuMTkgMjQuNjEgMTUuMjdRMjUuMDMgMTQuMzUgMjUuODMgMTMuODVRMjYuNjMgMTMuMzUgMjcuNjggMTMuMzVMMjcuNjggMTMuMzVRMjkuMDkgMTMuMzUgMjkuOTYgMTQuMTJRMzAuODIgMTQuODkgMzAuOTYgMTYuMjlMMzAuOTYgMTYuMjlMMjkuNDggMTYuMjlRMjkuMzggMTUuMzcgMjguOTQgMTQuOTZRMjguNTEgMTQuNTUgMjcuNjggMTQuNTVMMjcuNjggMTQuNTVRMjYuNzIgMTQuNTUgMjYuMjAgMTUuMjZRMjUuNjggMTUuOTYgMjUuNjcgMTcuMzNMMjUuNjcgMTcuMzNMMjUuNjcgMTguMDlRMjUuNjcgMTkuNDcgMjYuMTYgMjAuMjBRMjYuNjYgMjAuOTIgMjcuNjEgMjAuOTJMMjcuNjEgMjAuOTJRMjguNDggMjAuOTIgMjguOTIgMjAuNTNRMjkuMzYgMjAuMTQgMjkuNDggMTkuMjJMMjkuNDggMTkuMjJMMzAuOTYgMTkuMjJRMzAuODMgMjAuNTkgMjkuOTUgMjEuMzVRMjkuMDcgMjIuMTIgMjcuNjEgMjIuMTJMMjcuNjEgMjIuMTJRMjYuNTkgMjIuMTIgMjUuODIgMjEuNjNRMjUuMDQgMjEuMTUgMjQuNjIgMjAuMjZRMjQuMjAgMTkuMzcgMjQuMTggMTguMTlaTTM2Ljc1IDIyTDM1LjI3IDIyTDM1LjI3IDEzLjQ3TDM2Ljc1IDEzLjQ3TDM2Ljc1IDE3LjAyTDQwLjU3IDE3LjAyTDQwLjU3IDEzLjQ3TDQyLjA0IDEzLjQ3TDQyLjA0IDIyTDQwLjU3IDIyTDQwLjU3IDE4LjIxTDM2Ljc1IDE4LjIxTDM2Ljc1IDIyWk00Ni41MSAxOC4wMEw0Ni41MSAxOC4wMEw0Ni41MSAxNy41MlE0Ni41MSAxNi4yOCA0Ni45NiAxNS4zMlE0Ny40MCAxNC4zNyA0OC4yMCAxMy44NlE0OS4wMSAxMy4zNSA1MC4wNSAxMy4zNVE1MS4xMCAxMy4zNSA1MS45MCAxMy44NVE1Mi43MSAxNC4zNSA1My4xNSAxNS4yOVE1My41OSAxNi4yMyA1My41OSAxNy40OEw1My41OSAxNy40OEw1My41OSAxNy45NlE1My41OSAxOS4yMSA1My4xNiAyMC4xNlE1Mi43MyAyMS4xMCA1MS45MiAyMS42MVE1MS4xMSAyMi4xMiA1MC4wNiAyMi4xMkw1MC4wNiAyMi4xMlE0OS4wMyAyMi4xMiA0OC4yMiAyMS42MVE0Ny40MCAyMS4xMCA0Ni45NiAyMC4xN1E0Ni41MiAxOS4yMyA0Ni41MSAxOC4wMFpNNDguMDAgMTcuNDZMNDguMDAgMTcuOTZRNDguMDAgMTkuMzYgNDguNTQgMjAuMTNRNDkuMDkgMjAuOTAgNTAuMDYgMjAuOTBMNTAuMDYgMjAuOTBRNTEuMDUgMjAuOTAgNTEuNTggMjAuMTVRNTIuMTEgMTkuNDAgNTIuMTEgMTcuOTZMNTIuMTEgMTcuOTZMNTIuMTEgMTcuNTFRNTIuMTEgMTYuMDkgNTEuNTcgMTUuMzRRNTEuMDQgMTQuNTggNTAuMDUgMTQuNThMNTAuMDUgMTQuNThRNDkuMDkgMTQuNTggNDguNTUgMTUuMzNRNDguMDEgMTYuMDkgNDguMDAgMTcuNDZMNDguMDAgMTcuNDZaTTYzLjQxIDIyTDU4LjA2IDIyTDU4LjA2IDEzLjQ3TDU5LjU0IDEzLjQ3TDU5LjU0IDIwLjgyTDYzLjQxIDIwLjgyTDYzLjQxIDIyWk03Mi44OSAyMkw2Ny41NCAyMkw2Ny41NCAxMy40N0w2OS4wMiAxMy40N0w2OS4wMiAyMC44Mkw3Mi44OSAyMC44Mkw3Mi44OSAyMlpNNzguNTAgMjJMNzcuMDIgMjJMNzcuMDIgMTMuNDdMODAuMjggMTMuNDdRODEuNzEgMTMuNDcgODIuNTUgMTQuMjFRODMuMzkgMTQuOTYgODMuMzkgMTYuMThMODMuMzkgMTYuMThRODMuMzkgMTcuNDQgODIuNTcgMTguMTNRODEuNzUgMTguODMgODAuMjYgMTguODNMODAuMjYgMTguODNMNzguNTAgMTguODNMNzguNTAgMjJaTTc4LjUwIDE0LjY2TDc4LjUwIDE3LjY0TDgwLjI4IDE3LjY0UTgxLjA3IDE3LjY0IDgxLjQ5IDE3LjI3UTgxLjkwIDE2LjkwIDgxLjkwIDE2LjE5TDgxLjkwIDE2LjE5UTgxLjkwIDE1LjUwIDgxLjQ4IDE1LjA5UTgxLjA2IDE0LjY4IDgwLjMyIDE0LjY2TDgwLjMyIDE0LjY2TDc4LjUwIDE0LjY2Wk04OS4xNiAyMkw4Ny42OCAyMkw4Ny42OCAxMy40N0w5MC42OCAxMy40N1E5Mi4xNSAxMy40NyA5Mi45NiAxNC4xM1E5My43NiAxNC43OSA5My43NiAxNi4wNUw5My43NiAxNi4wNVE5My43NiAxNi45MCA5My4zNSAxNy40OFE5Mi45MyAxOC4wNiA5Mi4xOSAxOC4zN0w5Mi4xOSAxOC4zN0w5NC4xMSAyMS45Mkw5NC4xMSAyMkw5Mi41MiAyMkw5MC44MSAxOC43MUw4OS4xNiAxOC43MUw4OS4xNiAyMlpNODkuMTYgMTQuNjZMODkuMTYgMTcuNTJMOTAuNjggMTcuNTJROTEuNDMgMTcuNTIgOTEuODUgMTcuMTVROTIuMjggMTYuNzcgOTIuMjggMTYuMTFMOTIuMjggMTYuMTFROTIuMjggMTUuNDMgOTEuODkgMTUuMDVROTEuNTAgMTQuNjggOTAuNzIgMTQuNjZMOTAuNzIgMTQuNjZMODkuMTYgMTQuNjZaTTk3Ljg4IDE4LjAwTDk3Ljg4IDE4LjAwTDk3Ljg4IDE3LjUyUTk3Ljg4IDE2LjI4IDk4LjMzIDE1LjMyUTk4Ljc3IDE0LjM3IDk5LjU3IDEzLjg2UTEwMC4zOCAxMy4zNSAxMDEuNDIgMTMuMzVRMTAyLjQ3IDEzLjM1IDEwMy4yNyAxMy44NVExMDQuMDggMTQuMzUgMTA0LjUyIDE1LjI5UTEwNC45NiAxNi4yMyAxMDQuOTYgMTcuNDhMMTA0Ljk2IDE3LjQ4TDEwNC45NiAxNy45NlExMDQuOTYgMTkuMjEgMTA0LjUzIDIwLjE2UTEwNC4wOSAyMS4xMCAxMDMuMjkgMjEuNjFRMTAyLjQ4IDIyLjEyIDEwMS40MyAyMi4xMkwxMDEuNDMgMjIuMTJRMTAwLjQwIDIyLjEyIDk5LjU5IDIxLjYxUTk4Ljc3IDIxLjEwIDk4LjMzIDIwLjE3UTk3Ljg5IDE5LjIzIDk3Ljg4IDE4LjAwWk05OS4zNyAxNy40Nkw5OS4zNyAxNy45NlE5OS4zNyAxOS4zNiA5OS45MSAyMC4xM1ExMDAuNDYgMjAuOTAgMTAxLjQzIDIwLjkwTDEwMS40MyAyMC45MFExMDIuNDIgMjAuOTAgMTAyLjk1IDIwLjE1UTEwMy40OCAxOS40MCAxMDMuNDggMTcuOTZMMTAzLjQ4IDE3Ljk2TDEwMy40OCAxNy41MVExMDMuNDggMTYuMDkgMTAyLjk0IDE1LjM0UTEwMi40MSAxNC41OCAxMDEuNDIgMTQuNThMMTAxLjQyIDE0LjU4UTEwMC40NiAxNC41OCA5OS45MiAxNS4zM1E5OS4zOCAxNi4wOSA5OS4zNyAxNy40Nkw5OS4zNyAxNy40NlpNMTA4LjgyIDE5LjU3TDEwOC44MiAxOS41N0wxMTAuMzAgMTkuNTdRMTEwLjMwIDIwLjI1IDExMC42NCAyMC41OVExMTAuOTcgMjAuOTMgMTExLjYxIDIwLjkzTDExMS42MSAyMC45M1ExMTIuMjEgMjAuOTMgMTEyLjU2IDIwLjU0UTExMi45MiAyMC4xNCAxMTIuOTIgMTkuNDVMMTEyLjkyIDE5LjQ1TDExMi45MiAxMy40N0wxMTQuMzkgMTMuNDdMMTE0LjM5IDE5LjQ1UTExNC4zOSAyMC42OCAxMTMuNjMgMjEuNDBRMTEyLjg3IDIyLjEyIDExMS42MSAyMi4xMkwxMTEuNjEgMjIuMTJRMTEwLjI4IDIyLjEyIDEwOS41NSAyMS40NFExMDguODIgMjAuNzcgMTA4LjgyIDE5LjU3Wk0xMjQuNjUgMjJMMTE5LjA4IDIyTDExOS4wOCAxMy40N0wxMjQuNjEgMTMuNDdMMTI0LjYxIDE0LjY2TDEyMC41NiAxNC42NkwxMjAuNTYgMTcuMDJMMTI0LjA2IDE3LjAyTDEyNC4wNiAxOC4xOUwxMjAuNTYgMTguMTlMMTIwLjU2IDIwLjgyTDEyNC42NSAyMC44MkwxMjQuNjUgMjJaTTEyOC41OCAxOC4xOUwxMjguNTggMTguMTlMMTI4LjU4IDE3LjM5UTEyOC41OCAxNi4xOSAxMjkuMDEgMTUuMjdRMTI5LjQ0IDE0LjM1IDEzMC4yNCAxMy44NVExMzEuMDQgMTMuMzUgMTMyLjA4IDEzLjM1TDEzMi4wOCAxMy4zNVExMzMuNTAgMTMuMzUgMTM0LjM2IDE0LjEyUTEzNS4yMiAxNC44OSAxMzUuMzYgMTYuMjlMMTM1LjM2IDE2LjI5TDEzMy44OCAxNi4yOVExMzMuNzggMTUuMzcgMTMzLjM1IDE0Ljk2UTEzMi45MiAxNC41NSAxMzIuMDggMTQuNTVMMTMyLjA4IDE0LjU1UTEzMS4xMiAxNC41NSAxMzAuNjAgMTUuMjZRMTMwLjA4IDE1Ljk2IDEzMC4wNyAxNy4zM0wxMzAuMDcgMTcuMzNMMTMwLjA3IDE4LjA5UTEzMC4wNyAxOS40NyAxMzAuNTYgMjAuMjBRMTMxLjA2IDIwLjkyIDEzMi4wMSAyMC45MkwxMzIuMDEgMjAuOTJRMTMyLjg5IDIwLjkyIDEzMy4zMyAyMC41M1ExMzMuNzcgMjAuMTQgMTMzLjg4IDE5LjIyTDEzMy44OCAxOS4yMkwxMzUuMzYgMTkuMjJRMTM1LjIzIDIwLjU5IDEzNC4zNSAyMS4zNVExMzMuNDcgMjIuMTIgMTMyLjAxIDIyLjEyTDEzMi4wMSAyMi4xMlExMzAuOTkgMjIuMTIgMTMwLjIyIDIxLjYzUTEyOS40NCAyMS4xNSAxMjkuMDIgMjAuMjZRMTI4LjYwIDE5LjM3IDEyOC41OCAxOC4xOVpNMTQxLjM1IDE0LjY2TDEzOC43MiAxNC42NkwxMzguNzIgMTMuNDdMMTQ1LjQ4IDEzLjQ3TDE0NS40OCAxNC42NkwxNDIuODIgMTQuNjZMMTQyLjgyIDIyTDE0MS4zNSAyMkwxNDEuMzUgMTQuNjZaTTE1NC45NSAxOC4wMEwxNTQuOTUgMTguMDBMMTU0Ljk1IDE3LjUyUTE1NC45NSAxNi4yOCAxNTUuMzkgMTUuMzJRMTU1LjgzIDE0LjM3IDE1Ni42NCAxMy44NlExNTcuNDQgMTMuMzUgMTU4LjQ5IDEzLjM1UTE1OS41MyAxMy4zNSAxNjAuMzQgMTMuODVRMTYxLjE0IDE0LjM1IDE2MS41OCAxNS4yOVExNjIuMDIgMTYuMjMgMTYyLjAzIDE3LjQ4TDE2Mi4wMyAxNy40OEwxNjIuMDMgMTcuOTZRMTYyLjAzIDE5LjIxIDE2MS41OSAyMC4xNlExNjEuMTYgMjEuMTAgMTYwLjM1IDIxLjYxUTE1OS41NSAyMi4xMiAxNTguNTAgMjIuMTJMMTU4LjUwIDIyLjEyUTE1Ny40NiAyMi4xMiAxNTYuNjUgMjEuNjFRMTU1Ljg0IDIxLjEwIDE1NS40MCAyMC4xN1ExNTQuOTUgMTkuMjMgMTU0Ljk1IDE4LjAwWk0xNTYuNDMgMTcuNDZMMTU2LjQzIDE3Ljk2UTE1Ni40MyAxOS4zNiAxNTYuOTggMjAuMTNRMTU3LjUzIDIwLjkwIDE1OC41MCAyMC45MEwxNTguNTAgMjAuOTBRMTU5LjQ4IDIwLjkwIDE2MC4wMSAyMC4xNVExNjAuNTQgMTkuNDAgMTYwLjU0IDE3Ljk2TDE2MC41NCAxNy45NkwxNjAuNTQgMTcuNTFRMTYwLjU0IDE2LjA5IDE2MC4wMSAxNS4zNFExNTkuNDcgMTQuNTggMTU4LjQ5IDE0LjU4TDE1OC40OSAxNC41OFExNTcuNTMgMTQuNTggMTU2Ljk4IDE1LjMzUTE1Ni40NCAxNi4wOSAxNTYuNDMgMTcuNDZMMTU2LjQzIDE3LjQ2Wk0xNjcuOTcgMjJMMTY2LjQ5IDIyTDE2Ni40OSAxMy40N0wxNzEuOTEgMTMuNDdMMTcxLjkxIDE0LjY2TDE2Ny45NyAxNC42NkwxNjcuOTcgMTcuMjBMMTcxLjQxIDE3LjIwTDE3MS40MSAxOC4zOEwxNjcuOTcgMTguMzhMMTY3Ljk3IDIyWiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9Ik0xOTcuODkgMTcuODBMMTk3Ljg5IDE3LjgwUTE5Ny44OSAxNi41NCAxOTguNDkgMTUuNTRRMTk5LjA5IDE0LjU1IDIwMC4xNSAxMy45OVEyMDEuMjIgMTMuNDMgMjAyLjU3IDEzLjQzTDIwMi41NyAxMy40M1EyMDMuNzQgMTMuNDMgMjA0LjY4IDEzLjgzUTIwNS42MiAxNC4yMiAyMDYuMjQgMTQuOTdMMjA2LjI0IDE0Ljk3TDIwNC43MyAxNi4zM1EyMDMuODggMTUuNDAgMjAyLjcxIDE1LjQwTDIwMi43MSAxNS40MFEyMDIuNjkgMTUuNDAgMjAyLjY5IDE1LjQwTDIwMi42OSAxNS40MFEyMDEuNjEgMTUuNDAgMjAwLjk1IDE2LjA2UTIwMC4yOSAxNi43MSAyMDAuMjkgMTcuODBMMjAwLjI5IDE3LjgwUTIwMC4yOSAxOC41MCAyMDAuNTkgMTkuMDRRMjAwLjg5IDE5LjU5IDIwMS40MyAxOS44OVEyMDEuOTcgMjAuMjAgMjAyLjY3IDIwLjIwTDIwMi42NyAyMC4yMFEyMDMuMzUgMjAuMjAgMjAzLjk1IDE5LjkzTDIwMy45NSAxOS45M0wyMDMuOTUgMTcuNjJMMjA2LjA1IDE3LjYyTDIwNi4wNSAyMS4xMFEyMDUuMzMgMjEuNjEgMjA0LjM5IDIxLjg5UTIwMy40NiAyMi4xNyAyMDIuNTIgMjIuMTdMMjAyLjUyIDIyLjE3UTIwMS4yMCAyMi4xNyAyMDAuMTQgMjEuNjFRMTk5LjA5IDIxLjA1IDE5OC40OSAyMC4wNVExOTcuODkgMTkuMDYgMTk3Ljg5IDE3LjgwWk0yMTMuNDIgMjJMMjExLjA0IDIyTDIxMS4wNCAxMy42MEwyMTMuNDIgMTMuNjBMMjEzLjQyIDE2Ljc2TDIxNi42NiAxNi43NkwyMTYuNjYgMTMuNjBMMjE5LjAzIDEzLjYwTDIxOS4wMyAyMkwyMTYuNjYgMjJMMjE2LjY2IDE4LjcyTDIxMy40MiAxOC43MkwyMTMuNDIgMjJaTTIyMy43NyAxNy44MEwyMjMuNzcgMTcuODBRMjIzLjc3IDE2LjU1IDIyNC4zNyAxNS41NVEyMjQuOTcgMTQuNTYgMjI2LjA0IDE0LjAwUTIyNy4xMCAxMy40MyAyMjguNDMgMTMuNDNMMjI4LjQzIDEzLjQzUTIyOS43NiAxMy40MyAyMzAuODIgMTQuMDBRMjMxLjg5IDE0LjU2IDIzMi40OSAxNS41NVEyMzMuMTAgMTYuNTUgMjMzLjEwIDE3LjgwTDIzMy4xMCAxNy44MFEyMzMuMTAgMTkuMDUgMjMyLjQ5IDIwLjA0UTIzMS44OSAyMS4wNCAyMzAuODMgMjEuNjBRMjI5Ljc3IDIyLjE3IDIyOC40MyAyMi4xN0wyMjguNDMgMjIuMTdRMjI3LjEwIDIyLjE3IDIyNi4wNCAyMS42MFEyMjQuOTcgMjEuMDQgMjI0LjM3IDIwLjA0UTIyMy43NyAxOS4wNSAyMjMuNzcgMTcuODBaTTIyNi4xNiAxNy44MEwyMjYuMTYgMTcuODBRMjI2LjE2IDE4LjUxIDIyNi40NiAxOS4wNVEyMjYuNzcgMTkuNjAgMjI3LjI4IDE5LjkwUTIyNy44MCAyMC4yMCAyMjguNDMgMjAuMjBMMjI4LjQzIDIwLjIwUTIyOS4wNyAyMC4yMCAyMjkuNTggMTkuOTBRMjMwLjEwIDE5LjYwIDIzMC40MCAxOS4wNVEyMzAuNzAgMTguNTEgMjMwLjcwIDE3LjgwTDIzMC43MCAxNy44MFEyMzAuNzAgMTcuMDkgMjMwLjQwIDE2LjU0UTIzMC4xMCAxNiAyMjkuNTggMTUuNzBRMjI5LjA3IDE1LjQwIDIyOC40MyAxNS40MEwyMjguNDMgMTUuNDBRMjI3Ljc5IDE1LjQwIDIyNy4yOCAxNS43MFEyMjYuNzcgMTYgMjI2LjQ2IDE2LjU0UTIyNi4xNiAxNy4wOSAyMjYuMTYgMTcuODBaIiBmaWxsPSIjRkZGRkZGIiB4PSIxOTcuMTMiLz48L3N2Zz4=)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
