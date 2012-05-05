//
// Copyright (C) 2006-2007 Maciej Sobczak
// Distributed under the Boost Software License, Version 1.0.
// (See accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)
//

#ifndef REPORTS_H_INCLUDED
#define REPORTS_H_INCLUDED

#include "Reports.h"
#include <string>
#include <ostream>


namespace Vera
{
namespace Plugins
{


class Reports
{
public:
    typedef std::string FileName;
    typedef std::string Message;

    static void setShowRules(bool show);

    static void add(const FileName & name, int lineNumber, const Message & msg);

    static void dumpAll(std::ostream & os, bool omitDuplicates);
};

} // namespace Plugins

} // namespace Vera

#endif // REPORTS_H_INCLUDED
