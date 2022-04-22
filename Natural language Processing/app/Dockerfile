FROM continuumio/miniconda3

# Adding environment.yml to build the required context and create the environment

ARG conda_env=productionnlp
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

#to always run container add this to end of .bashrc script
# update the PATH environment variable using the ENV command 

RUN echo "source activate ${conda_env}" > ~/.bashrc
ENV PATH /opt/conda/envs/${conda_env}/bin:$PATH

ENV CONDA_DEFAULT_ENV $(head -1 /tmp/environment.yml | cut -d' ' -f2)

# finally start the jupyter notebook 
# using ENTRYPOINT used to configure container that runs as executable 

# start jupyter server on container 

EXPOSE 8888
ENTRYPOINT ["jupyter" , "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root","--no-browser"]
