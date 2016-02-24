<!--
.. title: Creating invoices with CouchDB.
.. date: 2009-02-11 22:10:21
.. author: Blake Winton
.. tags: couchdb, invoices, consulting, 1time
-->

A while ago I (and the rest of the company I worked for) was laid off, so I
was forcibly thrust into the world of consulting.  It’s been quite a
change, keeping track of my hours and sending out invoices for the work I
do.  And it’s that second point that I want to talk a little more about.

Perhaps I’m too picky, but there seemed to be a fatal flaw with all the
online invoicing tools I tried.  One didn’t allow enough clients for me on
the free plan.  (Yes, I am that cheap, especially when I’ve just been laid
off.)  Another would have allowed the client to dispute the invoice.  I
mean, really.  This is the invoice.  You don’t get to dispute it.  Or at
least, I don’t particularly want to make it easy for you.  So I ended up
using an [online time tracker](http://1timetracking.com/), and left the
invoice creation step until later.

Well, later rolled around, and I really kinda wanted to get paid, so I
downloaded a report of my hours [as a csv file](
http://1timetracking.com/#feature_tour), and whipped up a quick Python
script to parse it, and import it into a locally running copy of CouchDB.

The python script looked like this:

    #!python
    import couchdb.client
    import csv
    import path
    
    server = couchdb.client.Server('http://localhost:5984/')
    if 'timelog' not in server:
        db = server.create('timelog')
    
    db = server['timelog']
    print db
    
    def cleanup():
        # Clear out old rows.
        for row in db:
            if not row.startswith("_"):
                del db[row]
        
    def input( docName ):
        print docName
        input = open( docName )
        reader = csv.DictReader( input )
        i = 1
        for row in reader:
            row['Import Doc Name'] = docName
            row['Import Doc Row'] = i
            if 'Client Name' not in row:
              row['Client Name'] = "Client1"
            key = "%s_%03d" % (docName.name, i)
            print "  ", key
            db[key] = row
            i += 1
    
    cleanup()
    base = path.path("/Users/bwinton/Documents/Client1")
    for file in base.files("*.csv"):
        input( file )

Pretty easy, eh?  After that, I had to create a couple of CouchDB views:

    #!js
    // hoursPerDay
    map=function(doc) {
      key = [
        doc['Employee name'],
        doc['Client Name'],
        doc['Date of work'], 
      ];
      emit( key, doc );
    };
    reduce=function (tag, values) {
      sum=0;
      temp = []
      for( var i=0; i<values.length; i++ ) {
        sum += parseFloat(values[i]['Time in hours']);
        temp[i] = {
          'Order':values[i]['Import Doc Row'],
          'Description':values[i]['Description'],
          'Time':values[i]['Time in hours'],
          'Type':values[i]['Activity Type'],
        }
      }
      temp = temp.sort(function(a,b) {
        a = parseFloat(a['Order'])
        b = parseFloat(b['Order'])
        return a - b
      })
      return [sum, temp];
    };

    // totalHours
    // This view is just to save me re-calculating this value every time
    // I call the page, because it should only change when we add a new
    // document.
    map=function(doc) {
      key = [
        doc['Employee name'],
        doc['Client Name'],
        doc['Date of work'], 
      ];
      emit( key, parseFloat(doc['Time in hours']) );
    };
    reduce=function(keys, values, rereduce) {
      function sum( values )
      {
        retval = 0;
        for (i=0; i<values.length; i++)
        {
          retval += values[i];
        }
        return retval;
      }
      return sum(values);
    };

it was a quick snippet of HTML:

    #!html
    <html>
      <head><title>Time Log</title>
        <link rel="stylesheet" href="style/blueprint.css" type="text/css">
        <script>
          // Set up some variables.
          months = [ "2009-02" ]
          users = {
            "Blake Winton":{
              invoiceDates : [ "March 1st, 2009."],
              address : ["16 Forman Avenue",
                         "Toronto, ON, M4S 2R2",
                         "bwinton@latte.ca"]
            }};
        </script>
        <script src="script/bwTimesheet.js"></script>
      </head>
      <body>
        <p class="prepend-1"><b>Blake Winton</b><br/>
        16 Forman Avenue<br/>
        Toronto, ON, M4S 2R2<br/>
        bwinton@latte.ca</p>
        <p class="prepend-1"><b>Invoice Number:</b>
          XX-<span id="invoiceNum">000</span><br/>
        <b>Date:</b> <span id="invoiceDate">March 5th, 1973.</span><br/></p>
        
        <div class="prepend-1 span-1"><b>To:</b></div>
        <div class="span-22 last">
        Client Name<br/>
        16 Client Address</div>
        <p class="span-24">&nbsp;</p>
        <p><span id="timesheet">Timesheet loading...</span>
          <span id="summary">Summary loading...</span>
        </p>
      </body>
    </html>


and Javascript:

    #!js

    // Get a default month, if one wasn’t passed in.
    month = $.url.param('month')
    if (typeof(month) == 'undefined')
    {
      month = "0";
    }
    month = parseInt(month)
    if ( month < 0 || month >= months.length )
    {
      month = 0;
    }
    invoiceNumInt = month+1;
    month = months[month];

    // Get a default user, if one wasn’t passed in.
    // Yeah, I’ve defaulted it to me.  ;)
    user = $.url.param('user')
    if (typeof(user) == 'undefined')
    {
      user = "Blake Winton";
    }
    if (!(user in users))
    {
      user = "Blake Winton";
    }
    
    // Figure out when to start and end the invoice.
    invoiceDates = users[user].invoiceDates;
    invoiceDateStr = invoiceDates[invoiceNumInt-1];
    start = [user, client, month+"-01"];
    end = [user, client, month+"-31"];
    
    // Why, oh why, doesn’t Javascript have printf?
    function zeroPad(num,count)
    {
      var numZeropad = num + '';
      while(numZeropad.length < count)
      {
        numZeropad = "0" + numZeropad;
      }
      return numZeropad;
    }
    
    // Update the header, with the address, invoice number, and date.
    function updateHeader() {
      var address = $("#address").empty();
      address.append( "<b>"+user+"</b><br/>" );
      for (var i=0; i<users[user].address.length; i++)
      {
        var line = users[user].address[i];
        address.append( line + "<br/>" );
      }
    
      var invoiceNum = $("#invoiceNum").empty();
      invoiceNum.append( zeroPad( invoiceNumInt, 3 ));
    
      var invoiceDate = $("#invoiceDate").empty();
      invoiceDate.append( invoiceDateStr );
      updateTimesheet();
    }
    
    // Update the timesheet, with hours and descriptions.
    function updateTimesheet() {
      var timesheet = $("#timesheet").empty();
      var dbs = $.couch.db("timelog").view("invoice/hoursPerDay",{
        group: true,
        startkey: start,
        endkey: end,
        success: function(r) {
          table = "<div class='span-20 prepend-1 last'><table class='timelog'>";
          rowNum = 0;
          response = r['rows']
          for (var i = 0; i < response.length; i++) {
            var record = response[i];
            var date = record['key'][2];
            var total = record['value'][0];
            var entries = record['value'][1];
            table += "<tr class='row"+rowNum+"'><td>" +
            date + "</td><td>" +
            total + "h</td>";
            for (var j=0; j < entries.length; j++ )
            {
              if (j > 0)
              {
                table += "<tr class='row"+rowNum+"'><td/><td/>";
              }
              table += "<td>" + entries[j]['Time'] + "h - " +
                entries[j]['Description'] + "</td></tr>";
              rowNum += 1;
              rowNum %= 2;
            }
          }
          table += "</table></div>";
          timesheet.append( table );
          updateSummary();
        }
      })
    };
    
    // And finally, update the important stuff.
    // The total hours, rate, and amount owed.
    function updateSummary() {
      var dbs = $.couch.db("timelog").view("invoice/totalHours",{
        startkey: start,
        endkey: end,
        success: function(r) {
          summary = $("#summary").empty();
          content = "<p class='span-20 prepend-1 last'>";
          if ( r['rows'].length == 0 )
          {
            content += "No data available.";
          }
          else
          {
            value = r['rows'][0]['value'];
            content += "<b>Total hours:</b> " + value + "<br/>" +
              "<b>Rate:</b> $" + rate + currency +"/hour.<br/>" +
              "<b>Sub-total:</b> $" + (value*rate).toFixed(2) + "<br/>" +
              "<b>Tax (GST @ 5%):</b> $" + (value*5).toFixed(2) + "<br/>" +
              "<b>Total Payable:</b> $" + (value*(rate+5)).toFixed(2) + "<br/>"
              }
              content += "</p>";
              summary.append( content );
        }
      });
    };
          
    // When the document is ready, kick off the updates.
    $(function() {
      updateHeader();
    });
     
And we’re done.  Not to sound too much like an infomercial, but with [JQuery](
http://jquery.com/), [Blueprint]( http://www.blueprintcss.org/), [CouchDB](
http://couchdb.apache.org/), and [Python]( http://www.python.org/), it took me
only 255 lines of code to get a decent-enough-quality invoice that I could save
it as a PDF, send to the client, and get paid.  In fact, the client liked it
enough (or just wanted things to be standard enough) that they asked that the
other consultant on the project use the same template, so I had to spend some
time taking my original invoice script and editing it to support more than one
user.  Either way, I would call it a success.

