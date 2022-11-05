FROM python:3.10.6

EXPOSE 3000
WORKDIR /app

ADD  . /app

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt


ARG COMMIT_SHA=<not-specified>
RUN echo "mia_template_service_name_placeholder: $COMMIT_SHA" >> ./commit.sha


LABEL maintainer="%CUSTOM_PLUGIN_CREATOR_USERNAME%" \
      name="mia_template_service_name_placeholder" \
      description="%CUSTOM_PLUGIN_SERVICE_DESCRIPTION%" \
      eu.mia-platform.url="https://www.mia-platform.eu" \
      eu.mia-platform.version="0.1.0" \
      eu.mia-platform.language="Python" \
      eu.mia-platform.framework="FastAPI"

CMD ["python", "-m", "src.app"]