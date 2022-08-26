package Main;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import Statistics.VideoData;


public class WebScrape {
	
	public static VideoData getVideoData(String videoUrl) throws IOException {
	    Document doc = Jsoup.connect(videoUrl).header("User-Agent", "Chrome").get();
	    Element body = doc.body();
	    String videoThumbnail = body.getElementsByAttributeValue("itemprop", "thumbnailUrl").get(0).attr("href");
	    String videoEmbedUrl = body.getElementsByAttributeValue("itemprop", "embedURL").get(0).attr("href");
	    String videoTitle = body.getElementById("eow-title").attr("title");
	    Element user = body.getElementById("watch7-user-header");
	    String userLink = user.getElementsByAttributeValue("class", "yt-user-photo yt-uix-sessionlink      spf-link").attr("href");
	    String userPhoto = user.getElementsByTag("img").attr("data-thumb");
	    String channelLink = body.getElementById("watch7-user-header").getElementsByClass("yt-user-info").get(0).child(0).attr("href");
	    String channelName = body.getElementById("watch7-user-header").getElementsByClass("yt-user-info").get(0).child(0).wholeText();
	    boolean isChannelVerified;
	    try {
	        isChannelVerified = body.getElementById("watch7-user-header").getElementsByClass("yt-user-info").get(0).child(1).attr("aria-label").equalsIgnoreCase("Verified") ? true : false;
	    } catch (Exception e) {
	        isChannelVerified = false;
	    }
	    String noOfSubs = body.getElementsByClass("yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").attr("title");
	    String viewCount = body.getElementsByClass("watch-view-count").text();
	    String noOfLikes = body.getElementsByAttributeValue("title", "I like this").get(0).text();
	    String noOfDislikes = body.getElementsByAttributeValue("title", "I dislike this").get(0).text();
	    String publishedOn = body.getElementById("watch-uploader-info").text().replace("Published on ", "");
	    String description = body.getElementById("watch-description-text").children().text();
	    boolean isFamilyFriendly = body.getElementsByAttributeValue("itemprop", "isFamilyFriendly").attr("content").equalsIgnoreCase("True") ? true : false;
	    String genre = body.getElementsByAttributeValue("itemprop", "genre").attr("content");
	    VideoData videoData= new VideoData(videoThumbnail,videoEmbedUrl,videoTitle,userLink,userPhoto,channelLink,channelName,isChannelVerified,noOfSubs,viewCount,noOfLikes,noOfDislikes,publishedOn,description,isFamilyFriendly,genre);
	    return videoData;
	}
	
	
	
	
    public static void main(String[] args) throws IOException {
    	
    	
        	
            final String url = "https://www.google.com/search?q=funnyyoutube";//"https://www.youtube.com/results?search_query=funny+compilation+2022";
            		
            
                final Document document = Jsoup.connect(url).get();
                //System.out.println(document.getAllElements().outerHtml());
                
                
                Elements resultLinks = document.select("a[href]");
                for (Element e: resultLinks)
                {
//                    if(e.attr("href").indexOf("https://weather.com/weather/today")!=-1)
//                    {
                	//System.out.println(e.getElementsByAttribute("href").get(0));
                       // String nurl = e.attr("href");
                        //System.out.println(nurl);
                        //break;
                    //}
                }
                
                
                
//                System.out.println(document.outerHtml());
//               // System.out.println(document.getElementsByAttributeValue("class", "tile  tile--c--w  tile--vid  has-detail  opt--t-xxs").get(0));
//                
//                try(FileWriter fw = new FileWriter("C:\\Users\\William Marais\\Documents\\Computer Science Uni\\IDE-Workplace\\Youtube\\src\\Statistics\\html.txt", true);
//            		    BufferedWriter bw = new BufferedWriter(fw);
//            		    PrintWriter out = new PrintWriter(bw))
//            		{
//            		    out.println(document.getAllElements().outerHtml());
//            		    //more code
//            		    //out.println("more text");
//            		    //more code
//            		} catch (IOException e) {
//            		    //exception handling left as an exercise for the reader
//            		}
//	                //for (Element row : document.select("tbody tr")) {
//	    	
//	    	
	                //}
            
            
    	//getVideoData("");
    	
    }
}