#this is comment
FROM gcc:latest
MAINTAINER zhangt <zhangt@emicnet.com>
RUN mkdir /usr/src/myapp
COPY hello.c /usr/src/myapp/
WORKDIR /usr/src/myapp/
RUN gcc hello.c -o hello
CMD ["./hello"]

