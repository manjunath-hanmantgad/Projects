# to get all dbutils secrets help

# dbutils.secrets.help()

# list all the scopes present in workspace

# dbutils.secrets.listScopes()

# get all secrets present inside the scope

# dbutils.secrets.list("project-scope")

storage_account_name = "adlstorage01"
client_id            = dbutils.secrets.get(scope="project-scope", key="databricks-app-client-id")
tenant_id            = dbutils.secrets.get(scope="project-scope", key="databricks-app-tenant-id")
client_secret        = dbutils.secrets.get(scope="project-scope", key="databricks-app-client-secret")


configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}


def mount_adls(container_name):
      dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)
      

mount_adls("raw")

mount_adls("processed")

dbutils.fs.ls("/mnt/adlstorage01/raw")

dbutils.fs.ls("/mnt/adlstorage01/processed")


dbutils.fs.mounts()