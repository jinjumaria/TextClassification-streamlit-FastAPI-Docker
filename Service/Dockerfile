FROM python:3.8-slim

RUN adduser myuser
USER myuser

RUN pip install --upgrade pip
WORKDIR /home/myuser

COPY --chown=myuser:myuser ./requirements.txt .

ENV PATH="/home/myuser/.local/bin:${PATH}"

RUN pip install --user -r requirements.txt


COPY --chown=myuser:myuser . .

EXPOSE 8000

CMD ["python", "main.py"]
