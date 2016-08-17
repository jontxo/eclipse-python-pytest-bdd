var reporter = require('cucumber-html-reporter');

var options = {
        theme: 'bootstrap',
        jsonFile: './htmlReportGeneration/jasonReport.json',
        output: './htmlReportGeneration/cucumber_report.html',
        reportSuiteAsScenarios: true
    };

    reporter.generate(options);
