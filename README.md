# Video Sentiments
A small machine-learning algorithm to obtain speech segments from videos, and analyze the dominant sentiments in those speech segments.

**NOTE: This demo version will only work with videos which are <1 minute long.**

## Installation
### Setting up a Google Cloud Console Project
In this project, we use the Speech and Natural Language APIs from Google Cloud. To use services provided by Google Cloud, you must create a project.

A project organizes all your Google Cloud resources. A project consists of the following components:
- a set of collaborators
- enabled APIs (and other resources)
- monitoring tools
- billing information
- authentication and access controls

In the Google Cloud Console, on the [project selector page](https://console.cloud.google.com/projectselector2), select or create a Google Cloud project.

#### Enable Billing
A billing account is used to define who pays for a given set of resources, and it can be linked to one or more projects. Project usage is charged to the linked billing account. In most cases, you configure billing when you create a project.

Make sure that billing is [enabled for your Cloud project](https://cloud.google.com/billing/docs/how-to/modify-project).

#### Enable the APIs
Next step is to enable the APIs we need for our project.
1. Enable the [Cloud Speech-to-Text API](https://console.cloud.google.com/apis/library/speech.googleapis.com?_ga=2.214333783.1392152633.1610581150-535899091.1608141649).
2. Enable the [Cloud Natural Language API](https://console.cloud.google.com/flows/enableapi?apiid=language.googleapis.com&_ga=2.176585445.1392152633.1610581150-535899091.1608141649).

For more information on enabling APIs, see the [Service Usage documentation](https://cloud.google.com/service-usage/docs/enable-disable).

#### Set up authentication
1. In the Cloud Console, go to the [Create service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.14646903.1392152633.1610581150-535899091.1608141649) page.
2. From the **Service account** list, select **New service account**.
3. In the **Service account name** field, enter a name.
4. From the **Role** list, select **Project > Owner**.
5. Click **Create**. A JSON file that contains your key downloads to your computer.

Keep this JSON file secure and private. Provide authentication credentials to your application code by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to the JSON file you just downloaded. How you do this would depend on your operating system.

Replace [PATH] with the file path of the JSON file that contains your service account key. **This variable only applies to your current shell session, so if you open a new session, set the variable again!**

##### Linux or macOS
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

##### Windows
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]

### Running the Code
1. Clone the repository and `cd` to repository directory.
2. **Recommended.** Create a virtual environment for the project.
```
python3 -m venv venv/
source venv/bin/activate
```
3. Install project requirements
```
pip install -r requirements.txt
```
4. Run `python example.py --help` to see usage instructions.

For example, you can analyze sentiments in a video file and save the output to a `csv` by executing the script with the following options:
```
python example.py 'path/to/video.mp4' --save
```
[example.py](./example.py) demonstrates an example use case of the code. See the code to learn more.
