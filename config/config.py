# ------------------------------
# Unity Catalog Variables
# ------------------------------

# Catalog
catalog_name = "medisure_maxi"

# Schemas
schema_name_bronze = f"medisure_bronze"
schema_name_silver = f"medisure_silver"
schema_name_gold = f"medisure_gold"

# Volume
volume_name_landing = f"medisure_landing"
path_vol_landing = f"/Volumes/{catalog_name}/{schema_name_bronze}/{volume_name_landing}"
path_vol_landing_fact = f"{path_vol_landing}/facts"
path_vol_landing_ref = f"{path_vol_landing}/referentials"
path_vol_landing_historic = f"{path_vol_landing}/historic"

path_vol_landing_fact_claims_batch = f"{path_vol_landing_fact}/claims/claims_batch/raw"
path_vol_landing_fact_claims_stream = f"{path_vol_landing_fact}/claims/claims_stream/raw"
path_vol_landing_fact_claims_stream_checkpoint = f"{path_vol_landing_fact}/claims/claims_stream/checkpoint"

path_vol_landing_ref_diagnosis = f"{path_vol_landing_ref}/diagnosis_ref/raw"
path_vol_landing_ref_members = f"{path_vol_landing_ref}/members_ref/raw"
path_vol_landing_ref_providers = f"{path_vol_landing_ref}/providers_ref/raw"

# Input
file_input_claims_batch_csv = f"{path_vol_landing_fact_claims_batch}/claims_batch.csv"
file_input_claims_stream_json = f"{path_vol_landing_fact_claims_stream}/claims_stream.json"
file_input_diagnosis_ref_csv = f"{path_vol_landing_ref_diagnosis}/diagnosis_ref.csv"
file_input_members_csv = f"{path_vol_landing_ref_members}/members.csv"
file_input_providers_json = f"{path_vol_landing_ref_providers}/providers.json"

# Remote Input
path_url_claims_batch_csv = f"https://raw.githubusercontent.com/maxitan001/medisure_dbk/refs/heads/main/data/claims_batch.csv"
path_url_claims_stream_json = f"https://raw.githubusercontent.com/maxitan001/medisure_dbk/refs/heads/main/data/claims_stream.json"
path_url_diagnosis_ref_csv = f"https://raw.githubusercontent.com/maxitan001/medisure_dbk/refs/heads/main/data/diagnosis_ref.csv"
path_url_members_csv = f"https://raw.githubusercontent.com/maxitan001/medisure_dbk/refs/heads/main/data//members.csv"
path_url_providers_json = f"https://raw.githubusercontent.com/maxitan001/medisure_dbk/refs/heads/main/data/providers.json"

# Tables - bronze
bt_fact_claims_batch = f"{catalog_name}.{schema_name_bronze}.bt_fact_claims_batch"
bt_fact_claims_stream = f"{catalog_name}.{schema_name_bronze}.bt_fact_claims_stream"
bt_ref_diagnosis = f"{catalog_name}.{schema_name_bronze}.bt_ref_diagnosis"
bt_ref_members = f"{catalog_name}.{schema_name_bronze}.bt_ref_members"
bt_ref_providers = f"{catalog_name}.{schema_name_bronze}.bt_ref_providers"

# Tables - silver
st_fact_claims_merged = f"{catalog_name}.{schema_name_silver}.st_fact_claims_merged"
st_fact_claims_enriched = f"{catalog_name}.{schema_name_silver}.st_fact_claims_enriched"

st_ref_diagnosis_clean = f"{catalog_name}.{schema_name_silver}.st_ref_diagnosis_clean"
st_ref_members_clean = f"{catalog_name}.{schema_name_silver}.st_ref_members_clean"
st_ref_providers_clean = f"{catalog_name}.{schema_name_silver}.st_ref_providers_clean"

# Tables - gold
gt_fraud_signal = f"{catalog_name}.{schema_name_gold}.gt_fraud_signal"



# ------------------------------
# Groupings
# ------------------------------

# Unity Catalog schemas
schema_names = {
    "bronze": schema_name_bronze,
    "silver": schema_name_silver,
    "gold": schema_name_gold
}

#
path_input_files = [
    {
        "path_url": path_url_claims_batch_csv,
        "path_vol": file_input_claims_batch_csv
    },
    {
        "path_url": path_url_claims_stream_json,
        "path_vol": file_input_claims_stream_json
    },
    {
        "path_url": path_url_diagnosis_ref_csv,
        "path_vol": file_input_diagnosis_ref_csv
    },
    {
        "path_url": path_url_members_csv,
        "path_vol": file_input_members_csv
    },
    {
        "path_url": path_url_providers_json,
        "path_vol": file_input_providers_json
    }

]
