FROM public.ecr.aws/lambda/python:3.6

RUN pip install \
	numpy==1.17.3 \
	scikit-learn==0.23.1 \
	pandas==0.25.2 \
	tqdm==4.36.1

COPY . ./

CMD ["main.handler"]

