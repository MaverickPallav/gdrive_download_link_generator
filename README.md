Make sure the link sharing option is set to (Anyone with the link) option

To run locally

```bash
python3 main.py url
```

To create a webapp using streamlit

```bash
pip install streamlit
streamlit run app_streamlit.py
```
To run native mac and win application

```bash
cd electron
npm i
chmod +x run_streamlit.sh
npm start
```

To bundle native mac and win application
```bash
cd electron
npm i
chmod +x run_streamlit.sh
npx electron-packager . StreamlitApp --platform=win32 --arch=x64 --out=dist/
npx electron-packager . StreamlitApp --platform=darwin --arch=x64 --out=dist/
```
