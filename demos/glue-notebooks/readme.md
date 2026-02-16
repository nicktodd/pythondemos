# AWS Glue Notebooks Lab

## Overview
In this lab, you will create and work with AWS Glue Notebooks to run PySpark exercises on AWS infrastructure. AWS Glue is a fully managed ETL (Extract, Transform, Load) service that makes it easy to prepare and transform data for analytics.

## Prerequisites
- AWS Account access with provided credentials
- The starter notebook file from this directory: `SparkExercisesStarterNotebook.ipynb`
- Access to the S3 buckets: `s3://spark.demo.data/` and `s3://spark.labs.saves/`

## Step-by-Step Instructions

### Step 1: Sign in to AWS Console
1. Navigate to the AWS Management Console
2. Sign in using the provided credentials
3. Ensure you are in the correct AWS region (check with your instructor)

### Step 2: Navigate to AWS Glue
1. In the AWS Console search bar at the top, type **"Glue"**
2. Click on **"AWS Glue"** from the search results
3. This will take you to the AWS Glue dashboard

### Step 3: Access Glue Studio
1. In the left navigation pane, expand the **"ETL Jobs"** section
2. Click on **"Notebooks"** under the ETL Jobs section
3. This will display the Notebooks page

### Step 4: Create a New Notebook
1. Click the **"Create notebook"** button (or **"Jupyter Notebook"** option)
2. You will see options to create a notebook

### Step 5: Upload the Starter Notebook
1. Select the option **"Upload and edit an existing notebook"**
2. Click **"Choose file"** or **"Browse"**
3. Navigate to this directory (`demos/glue-notebooks/`)
4. Select the file: **`SparkExercisesStarterNotebook.ipynb`**
5. Click **"Open"** to upload the file

### Step 6: Configure the Notebook
1. **Notebook name**: Give your notebook a meaningful name (e.g., "PySpark-Exercises-YourName")
2. **IAM Role**: 
   - Select **"Choose an existing IAM role"**
   - From the dropdown, select: **`GlueServiceRoleWatchelm`**
3. Review other settings (you can typically leave them as default):
   - **Glue version**: 4.0 (or latest available)
   - **Language**: Python 3
   - **Worker type**: G.1X (default)
   - **Number of workers**: 2 (default)

### Step 7: Create and Start the Notebook
1. Click **"Create notebook"** button at the bottom
2. Wait for the notebook to be created (this may take 1-2 minutes)
3. The notebook will automatically start provisioning resources
4. Once ready, you'll see the Jupyter notebook interface

### Step 8: Start an Interactive Session
1. The first cell in the notebook contains information about Glue Studio magics
2. Before you can run any code, you need to start an interactive session
3. Run the second cell (the one with imports and configuration)
4. Wait for the session to start - you'll see a progress indicator
5. Session startup typically takes 2-3 minutes

### Step 9: Verify Configuration
1. Check that the `data_bucket_url` variable is set to: `s3://spark.demo.data/`
2. Check that the `lab_output_bucket_url` variable is set to: `s3://spark.labs.saves/`
3. These should already be configured in the notebook

### Step 10: Begin Working Through Exercises
1. Follow the instructions in each notebook cell
2. Run cells one at a time using **Shift + Enter** or the ▶️ button
3. Complete the exercises as described in the markdown cells
4. Replace `None` values with appropriate PySpark code

## Important Notes

### Session Management
- Glue sessions will automatically timeout after 60 minutes of inactivity
- To check your session status, run: `%status`
- To manually stop a session (to save costs), run: `%stop_session`
- Always stop your session when finished!

### Saving Your Work
- The notebook auto-saves periodically
- You can manually save using **File > Save** or **Ctrl + S**
- Your notebook is stored in your AWS account
- Make sure to download your completed notebook if you want a local copy

### S3 Bucket Access
- The exercises read data from `s3://spark.demo.data/`
- You can save outputs to `s3://spark.labs.saves/`
- Make sure the IAM role `GlueServiceRoleWatchelm` has permissions to access these buckets

### Troubleshooting

**Problem**: "Access Denied" errors when accessing S3
- **Solution**: Verify you're using the `GlueServiceRoleWatchelm` IAM role

**Problem**: Session won't start
- **Solution**: Check that you have available capacity in your AWS account. Contact your instructor if issues persist.

**Problem**: "Kernel not found" or connection errors
- **Solution**: Refresh the browser page and wait for the session to fully initialize

**Problem**: Code cells not executing
- **Solution**: Make sure you've run the initialization cell (Cell 2) first and waited for the session to start

## Cost Considerations
- AWS Glue charges for the time your notebook session is active
- Always remember to **stop your session** when you're done
- To stop: Click the ⏹️ stop button or run `%stop_session` magic command

## Additional Resources
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [PySpark API Documentation](https://spark.apache.org/docs/latest/api/python/)
- [AWS Glue Studio User Guide](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html)

## Completion
After completing all exercises:
1. Save your notebook
2. Stop your Glue session using `%stop_session`
3. Download your completed notebook: **File > Download**
4. Optionally, check your S3 bucket for output files

Good luck with your PySpark exercises!
