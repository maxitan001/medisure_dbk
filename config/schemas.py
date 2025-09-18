from pyspark.sql.types import *

# Schema for input claims_batch
schema_claims_batch = StructType([
	StructField('ClaimID', StringType(), True),
	StructField('MemberID', StringType(), True),
	StructField('ProviderID', StringType(), True),
	StructField('ClaimDate', DateType(), True),
	StructField('ServiceDate', DateType(), True),
	StructField('Amount', DoubleType(), True),
	StructField('Status', StringType(), True),
	StructField('ICD10Codes', StringType(), True),
	StructField('CPTCodes', StringType(), True),
	StructField('ClaimType', StringType(), True),
	StructField('SubmissionChannel', StringType(), True),
	StructField('Notes', StringType(), True),
	StructField('IngestTimestamp', TimestampType(), True)
])


# Schema for input claims_stream
schema_claims_stream = StructType([
	StructField('Amount', DoubleType(), True),
	StructField('CPTCodes', StringType(), True),
	StructField('ClaimDate', StringType(), True),
	StructField('ClaimID', StringType(), True),
	StructField('EventTimestamp', StringType(), True),
	StructField('ICD10Codes', StringType(), True),
	StructField('MemberID', StringType(), True),
	StructField('ProviderID', StringType(), True),
	StructField('Status', StringType(), True)
])


# Schema for input diagnosis_ref
schema_diagnosis_ref = StructType([
	StructField('Code', StringType(), True),
	StructField('Description', StringType(), True)
])


# Schema for input members
schema_members = StructType([
	StructField('MemberID', StringType(), True),
	StructField('Name', StringType(), True),
	StructField('DOB', DateType(), True),
	StructField('Gender', StringType(), True),
	StructField('Region', StringType(), True),
	StructField('PlanType', StringType(), True),
	StructField('EffectiveDate', DateType(), True),
	StructField('Email', StringType(), True),
	StructField('IsActive', DoubleType(), True),
	StructField('LastUpdated', DateType(), True)
])


# Schema for input providers
schema_providers = StructType([
	StructField('IsActive', BooleanType(), True),
	StructField('LastVerified', StringType(), True),
	StructField('Locations', ArrayType(StructType([
		StructField('Address', StringType(), True),
		StructField('City', StringType(), True),
		StructField('State', StringType(), True
	)]), True), True),
	StructField('Name', StringType(), True),
	StructField('ProviderID', StringType(), True),
	StructField('Specialties', ArrayType(
		StringType(), True), True),
	StructField('TIN', StringType(), True)
])