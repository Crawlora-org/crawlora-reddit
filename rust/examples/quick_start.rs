use crawlora_reddit::{Client, ModelRedditSearchResponseDoc, RedditSearchParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .reddit
        .search(RedditSearchParams {
            q: Some("open source".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelRedditSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
