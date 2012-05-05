//
// Copyright (C) 2006-2007 Maciej Sobczak
// Distributed under the Boost Software License, Version 1.0.
// (See accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)
//

#ifndef PROFILES_H_INCLUDED
#define PROFILES_H_INCLUDED

#include <string>
#include <stdexcept>


namespace Vera
{
namespace Plugins
{


class ProfileError : public std::runtime_error
{
public:
    ProfileError(const std::string & msg) : std::runtime_error(msg) {}
};

class Profiles
{
public:
    typedef std::string ProfileName;

    static void executeProfile(const ProfileName & name);
};

} // namespace Plugins

} // namespace Vera

#endif // PROFILES_H_INCLUDED
