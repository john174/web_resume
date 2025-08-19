# Web Resume

Static resume site for Evgeniy Kalinin.

## Deployment

This site is configured for Netlify. The published files live in the `public` directory and no build step is required.  
Stylesheets and scripts are organized under `public/css` and `public/js` for clarity.

1. Connect the repository to Netlify.
2. Leave the **Base directory** empty (use repository root).
3. Set the **Publish directory** to `public`.
4. There is no build command.

After deployment, the resume will be available at the site URL.

## Streamlit Version

The repository also includes `streamlit_app.py` which renders the resume using [Streamlit](https://streamlit.io/).

### Local development

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
